import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import os.path
from os import path
import csv
import pickle

from Curling_League_App.competition import Competition
from Curling_League_App.identified_object import IdentifiedObject
from Curling_League_App.league_database import LeagueDatabase
from Curling_League_App.team import Team
from Curling_League_App.team_member import TeamMember
from Curling_League_App.exceptions.duplicate_oid import DuplicateOid
from Curling_League_App.exceptions.duplicate_email import DuplicateEmail
from Curling_League_App.league import League


Ui_MainWindow, QtBaseWindow = uic.loadUiType("main_window.ui")

class MainWindow(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.leagues = LeagueDatabase.the_leagues
        self.setupUi(self)
        self.action_load.triggered.connect(self.browseFile)
        self.add_button.clicked.connect(self.addLeague)
        self.remove_button.clicked.connect(self.removeLeague)

    def browseFile(self):
        fname=QFileDialog.getOpenFileName(self, "Open File")
        file = open(fname[0], 'rb')
        for row in file:
            self.leagues.append(row)
            #self.league_list_widget.addItem(row)
        self.update_ui()

        #league_database.load(fname[0])
        #with open(fname, newline='', encoding="utf-8") as csvfile:
            #read_file = csv.reader(csvfile, quoting=csv.QUOTE_NONE)
            #next(read_file)
            #for row in read_file:
                #self.league_list_widget.addItem(row)


    def update_ui(self):
        self.league_list_widget.clear()
        for item in self.leagues:
            self.league_list_widget.addItem(str(item))

    def addLeague(self):
        add_item = QtWidgets.QInputDialog.getText(self, "Add League", "Enter league name:")
        #result = add_item.exec()
        if add_item[1]:
            new_league = League(LeagueDatabase._last_oid, add_item[0])
            self.leagues.append(add_item[0])
            self.update_ui()
            print(LeagueDatabase.the_leagues)
            #self.league_list_widget.addItem(add_item[0])
        else:
            print("canceled")

    def removeLeague(self):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Icon.Question)
        dialog.setWindowTitle("Remove League")
        dialog.setText("Are you sure you want to delete this league from the list?")
        no = dialog.addButton("No", QMessageBox.ButtonRole.RejectRole)
        yes = dialog.addButton("Yes", QMessageBox.ButtonRole.AcceptRole)

        dialog.exec()
        if dialog.clickedButton() == yes:
            del self.leagues[self.league_list_widget.currentRow()]
            self.update_ui()
        else:
            print("No")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())