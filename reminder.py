from PyQt5 import QtWidgets, uic

from PyQt5.QtWidgets import QLabel, QWidget

from config import UI_MAIN_WINDOW, DESIGN_DIR

# Read more at
# https://doc.bccnsoft.com/docs/PyQt5/designer.html#using-the-generated-code
Ui_MainWindow, _ = uic.loadUiType(UI_MAIN_WINDOW, import_from=DESIGN_DIR)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    '''
    При открытии программы выводить записи из "reminder.txt" в браузер
    При нажатии на кнопку "Добавить" выводить в браузер все записи включая новую
    При закрытии программы сохранить всё в "reminder.txt"
    '''
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # self.user_input = ''
        self.setupDesign()
        with open('reminder.txt', 'r') as file:
            self.user_input = file.read().strip() + '\n'
        self.addReminder()

    def setupDesign(self):
        self.add_pushButton.released.connect(self.addReminder)
        self.delete_pushButton.released.connect(self.deleteReminder)

    def addReminder(self):
        if self.add_lineEdit.text() != '':
            newRemineder = self.add_lineEdit.text().replace('\n', ' ').strip(' ')
            self.user_input += newRemineder + '\n'
            self.textBrowser.setText(self.user_input)
            self.add_lineEdit.clear()
        else:
            self.textBrowser.setText(self.user_input)

    def closeEvent(self, event):
        with open('reminder.txt', 'w') as file:
            file.write(self.user_input)