from PyQt5.QtWidgets    import  (QTableView,
                                QHeaderView,
                                QAbstractItemView,
                                QStyledItemDelegate)
from PyQt5.QtCore       import  (Qt,
                                QMimeData,
                                QModelIndex,
                                QRect,
                                QAbstractItemModel,
                                QVariant,
                                QDateTime)
from PyQt5.QtGui        import  (QColor,
                                QPainter,
                                QBrush,
                                QPen,
                                QCursor,
                                QPixmap,
                                QDrag)
from QtSpreadSheetModel import QSpreadSheetModel
from QtSpreadSheetItemDelegate import QSpreadSheetItemDelegate
from functions import paintEvent, mouse
import datetime
import traceback
import ExcelFunctionality as ef
import numpy as np
import pandas as pd
import re
import os

class QSpreadSheetWidget(QTableView):
    """
    The QSpreadSheetWidget class is a subclass of QTableView that provides 
    additional functionality to the tableview in order to get it to behave like an
    excel spreadsheet.
    """

    def __init__(self, parent = None, *args, **kwargs):
        """
        Constructor for the class. Here we initialize an empty model,
        and initialize the stylesheet for the widget.

        kwargs:
            'highlightColor': RGB color [#ffffff or (255, 255, 255) format] 
        """
        QTableView.__init__(self)
        self.parent = parent

        # Create new, empty QAbstractItemModel for the spreadsheet
        self.setModel(QSpreadSheetModel())

        # Set the default cursor
        self.cursor_ = QCursor(QPixmap('cursor.bmp'))
        self.setCursor(self.cursor_)
        self.setMouseTracking(True)

        # State Variable
        # N: Normal Operation
        # D: Dragging Selection
        # S: Selecting Range in cell edit
        # F: Filling Using Fill Handle
        self.state_ = 'N'

        # Set an item delegate
        self.delegate = QSpreadSheetItemDelegate(self)
        self.setItemDelegate(self.delegate)

        # Set the higlight color
        if 'highlightColor' in list(kwargs.keys()):
            color = kwargs['highlightColor']
            if isinstance(color, tuple):
                self.highlightColor = QColor(*color)
            else:
                self.highlightColor = QColor(color)
        else:
            self.highlightColor = QColor(66, 134, 244)

        # Set the widgets' stylesheet
        colorCode = '#%02x%02x%02x' % (self.highlightColor.red(), self.highlightColor.green(), self.highlightColor.blue())
        print(colorCode)
        self.setStyleSheet(open(os.path.abspath('style.qss'), 'r').read().format(colorCode))
        
        return


    def paintEvent(self, event):
        paintEvent.paintEvent(self, event)

    def mouseMoveEvent(self, event):
         mouse.mouseMoveEvent(self, event)

    def mousePressEvent(self, event):
        mouse.mousePressEvent(self, event)

    # def mouseReleaseEvent(self, event):
    #     mouse.mouseReleaseEvent(self, event)

    def keyPressEvent(self, event):
        """
        """
        QTableView.keyPressEvent(self, event)
        if event.key() == Qt.Key_Delete and self.state_=='N':
            selections = self.selectionModel().selection()
            for selection in selections:
                indexes = selection.indexes()
                for index in indexes:
                    self.model().setData(index, "%DELETEDATA%")
        
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and self.state_=='N':
            ind = self.currentIndex()
            ind = ind.sibling(ind.row()+1, ind.column())
            self.setCurrentIndex(ind)
        
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return) and self.state_=='S':
            self.model().setData(self.delegate.index, self.delegate.editor.text())
            self.closeEditor(self.delegate.editor, 0, True)
            ind = self.currentIndex()
            ind = ind.sibling(ind.row()+1, ind.column())
            self.setCurrentIndex(ind)
        
        return


    def edit(self, index, trigger, event):
        """
        """
        value = QTableView.edit(self, index, trigger, event)
        if int(trigger) in [2, 8, 16]:
            self.state_ = 'S'

        return value


    def closeEditor(self, editor, hint, close=False):
        """
        """
        if editor.text() == '':
            val = QTableView.closeEditor(self, editor, hint)
            self.state_ = 'N'
            return val
        if editor.text().strip()[0] == '=' and close==False:
            return
        val = QTableView.closeEditor(self, editor, hint)
        self.state_ = 'N'

        return val

    def commitData(self, editor):
        """
        """
        if self.state_ == 'S':
            return
        val = QTableView.commitData(self, editor)
        return val

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
    import sys
    #data = pd.DataFrame(np.random.random((30,4))).astype('object')
    data = pd.read_excel('tests/PointDatasets.xlsx').astype('object')
    application = QApplication(sys.argv)
    mw = QSpreadSheetWidget(highlightColor='#000000')
    mw.show()
    mw.model().load_new_dataset(data)
    def run_():
        return_value = application.exec_()
        print(data)
        return return_value
    sys.exit(run_())



