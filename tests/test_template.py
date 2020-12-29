import pytest
from pytestqt.qt_compat import qt_api

from qt.app import MainWindow


def test_basics(qtbot):
    """
    Basic test that works more like a sanity check to ensure we are setting up a QApplication
    properly and are able to display a simple event_recorder.
    """

    assert qt_api.QApplication.instance() is not None
    widget = qt_api.QWidget()
    qtbot.addWidget(widget)
    widget.setWindowTitle("W1")
    widget.show()
    assert widget.isVisible()
    assert widget.windowTitle() == "W1"

def test_main_window(qtbot):
    """
    Same as above but testing the main window of template package
    """

    assert qt_api.QApplication.instance() is not None
    mw = MainWindow()
    qtbot.addWidget(mw)
    mw.show()
    assert mw.isVisible()
