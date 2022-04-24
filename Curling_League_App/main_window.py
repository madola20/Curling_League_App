import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDialog

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

from Curling_League_App.edit_dialog import EditDialog


Ui_MainWindow, QtBaseWindow = uic.loadUiType("main_window.ui")

class MainWindow(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.leagues = LeagueDatabase.the_leagues
        self.setupUi(self)
        self.action_load.triggered.connect(self.browseFile)
        self.action_save.triggered.connect(self.saveFile)
        self.add_button.clicked.connect(self.addLeague)
        self.remove_button.clicked.connect(self.removeLeague)
        self.edit_button.clicked.connect(self.editLeague)

        self.theDatabase = LeagueDatabase()

    def browseFile(self):
        """
        fname=QFileDialog.getOpenFileName(self, "Open File")
        file = open(fname[0], 'rb')
        for row in file:
            self.leagues.append(row)
            #self.league_list_widget.addItem(row)
        self.update_ui()
        """
        fname = QFileDialog.getOpenFileName(self, "Open File")
        f = open(fname[0], mode="rb")
        ba = pickle.load(f)
        print(str(ba))
        for item in ba:
            #self.league_list_widget.addItem(str(item))
            self.leagues.append(item)
        self.update_ui()

        f.close()

        #league_database.load(fname[0])
        #with open(fname, newline='', encoding="utf-8") as csvfile:
            #read_file = csv.reader(csvfile, quoting=csv.QUOTE_NONE)
            #next(read_file)
            #for row in read_file:
                #self.league_list_widget.addItem(row)

    def saveFile(self):
        fname = QFileDialog.getSaveFileName(self, 'Save File')
        f = open(fname[0], mode="wb")

        pickle.dump([self.leagues], f)
        f.close()


    def update_ui(self):
        self.league_list_widget.clear()
        for item in self.leagues:
            self.league_list_widget.addItem(str(item))

    def addLeague(self):
        add_item = QtWidgets.QInputDialog.getText(self, "Add League", "Enter league name:")
        #result = add_item.exec()
        if add_item[1]:
            new_league = League(LeagueDatabase._last_oid, add_item[0])
            self.theDatabase.next_oid()
            self.leagues.append(new_league)
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

    def editLeague(self):
        row = self.league_list_widget.currentRow()
        selected_league = self.leagues[row]
        dialog = EditDialog(selected_league)
        if dialog.exec() == QDialog.DialogCode.Accepted:

            self.update_ui()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())