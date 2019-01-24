from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtCore import Qt

class QSpreadSheetItemDelegate(QStyledItemDelegate):

    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self)
    
    def createEditor(self, parent, option, index):
        self.index = index
        self.editor = QStyledItemDelegate.createEditor(self, parent, option, index)
        return self.editor