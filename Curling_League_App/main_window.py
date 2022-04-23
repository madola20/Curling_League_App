import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import os.path
from os import path
import csv
import pickle

from Curling_League_App import competition, identified_object, league, league_database, team, team_member, exceptions

Ui_MainWindow, QtBaseWindow = uic.loadUiType("main_window.ui")

class MainWindow(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.action_load.triggered.connect(self.browseFile)

    def browseFile(self):
        fname=QFileDialog.getOpenFileName(self, "Open File")
        #league_database.load(fname)
        with open(fname, newline='', encoding="utf-8") as csvfile:
            read_file = csv.reader(csvfile, quoting=csv.QUOTE_NONE)
            #next(read_file)
            for row in read_file:
                self.league_list_widget.addItem(row)







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())