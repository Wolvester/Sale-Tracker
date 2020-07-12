from PyQt5 import QtWidgets, uic
import sys
import Kickstarter_Scrapper

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('//10.0.0.16/files/Projects/Website Scrapper/basic.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'runBtn')
        self.button.clicked.connect(self.runBtnPressed)
        self.text = self.findChild(QtWidgets.QTextEdit, 'outputTxt')

        self.show()

    def runBtnPressed(self):
        if Kickstarter_Scrapper.scrapeKickstart() is True:
            self.text.setText('There are only ' + str(Kickstarter_Scrapper.getAvailableRewards()) + ' rewards left!')
        else:
            self.text.setText(Kickstarter_Scrapper.getResults())


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
