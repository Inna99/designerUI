def initate_application() -> None:
    """Application entry point."""
    import sys
    from PyQt5 import QtWidgets
    from reminder import MainWindow
    from utils.win import set_current_process_explicit_attributes

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    initate_application()
