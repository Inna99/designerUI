"""Helpers for Windows OS."""


import ctypes
from config import MY_COMPANY, MY_PRODUCT, MY_SUBPRODUCT, VERSION


def set_current_process_explicit_attributes() -> None:
    """
    This function tells windows not to treat application as a python script
    But rather as an independent executable.
    It allows to set up custom icon in task bar
    Information about company, product and version is available in windows services

    Original source:
    https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105
    """

    myappid = '.'.join((MY_COMPANY, MY_PRODUCT, MY_SUBPRODUCT, VERSION))
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'{}'.format(myappid))
