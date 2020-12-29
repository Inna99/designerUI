from PyQt5 import QtCore, QtGui, QtWidgets


class BaseWindowWidget(QtWidgets.QWidget):
    """Base Window Class."""


class MoveableWidget(BaseWindowWidget):
    """
    Inheritance from this class will make your widget moveable with mouse
    It's helpful in case your widget is frameless
    """

    _widget_position: QtCore.QPoint

    def center(self) -> None:
        """ Centering main window / widget """

        qr: QtCore.QRect = self.frameGeometry()
        cp: QtCore.QPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """ Save cursor position (x, y) in a class variable """

        self._widget_position: QtCore.QPoint = event.globalPos()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Save delta of old (x, y) position, then move widget to new position
        And store it in a class
        """
        delta: QtCore.QPoint = event.globalPos() - self._widget_position
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self._widget_position = event.globalPos()
