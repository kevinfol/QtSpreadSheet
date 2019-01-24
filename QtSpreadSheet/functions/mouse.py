from PyQt5.QtWidgets import (QTableView)
from PyQt5.QtCore import (QModelIndex,
                         Qt)
from PyQt5.QtGui import (QCursor)

def mouseMoveEvent(self, event):
    """
    Checks the position of the mouse and change the cursor accordingly. 
    If the cursor is in the middle of a range selection, keep track of the range
    and update the edit box accordingly.
    """
    QTableView.mouseMoveEvent(self, event)
    pos = event.pos()
    x = pos.x()
    y = pos.y()

    if self.state_ == 'D':
        if (pos - self.dragStartPosition).manhattanLength() < 4:
            return
    
        return
    
    if self.state_ == 'N':
        selections = self.selectionModel().selection()
        if len(selections) == 1:

            topLeft = self.visualRect(QModelIndex(selections[0].topLeft()))
            bottomRight = self.visualRect(QModelIndex(selections[0].bottomRight()))
            left = topLeft.left()
            right = bottomRight.right()
            top = topLeft.top()
            bottom = bottomRight.bottom()

        else:
            self.viewport().update()
            return
        
        if x > left and x < right and y > top - 3 and y < top + 3:
            self.setCursor(QCursor(Qt.OpenHandCursor))
            self.viewport().update()
            return
        if x > left - 3 and x < left + 3 and y > top and y < bottom:
            self.setCursor(QCursor(Qt.OpenHandCursor))
            self.viewport().update()
            return
        if x > right - 3 and x < right + 5 and y > top and y < bottom + 5:
            if y > bottom - 5 and y < bottom + 5:
                
                self.setCursor(QCursor(Qt.CrossCursor))
                self.viewport().update()
                return
            self.setCursor(QCursor(Qt.OpenHandCursor))
            self.viewport().update()
            return
        if x > left and x < right + 5 and y > bottom - 3 and y < bottom + 3:
            if x > right - 5 and x < right + 5:
                
                self.setCursor(QCursor(Qt.CrossCursor))
                self.viewport().update()
                return
            self.setCursor(QCursor(Qt.OpenHandCursor))
            self.viewport().update()
            return
        viewport = self.viewport().rect()
        xl = viewport.left()
        xr = viewport.right()
        yt = viewport.top()
        yb = viewport.bottom()
        if x < xr and x > xl and y < yb and y > yt:
            self.setCursor(self.cursor_)
        else:
            self.setCursor(QCursor(Qt.ArrowCursor))
        self.viewport().update()
        return
    return

    if self.state_ == 'S':
        # Get index / location of mouse cursor
        # figure out selection
        # figure out range string
        # add range string to cell editor
        # paint selection
        return

def mousePressEvent(self, event):
    if self.state_ == 'S':
        # Get index/location of click
        # make sure it's not the cell we're editing
        # store cell in range string
        # add range string to cell editor
        # paint selection
        return
    QTableView.mousePressEvent(self, event)
    return

def mouseReleaseEvent(self, event):
    if self.state_ == 'S':
        return
    return