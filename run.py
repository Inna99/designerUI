def initate_application() -> None:
    """Application entry point."""
    import sys
    import platform
    from PyQt5 import QtWidgets
    from app import MainWindow
    from utils.win import set_current_process_explicit_attributes

    if platform.system() == 'Windows':
        set_current_process_explicit_attributes()

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    initate_application()
