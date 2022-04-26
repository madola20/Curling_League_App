from PyQt5 import uic, QtWidgets
import sys

from PyQt5.QtWidgets import QMessageBox, QFileDialog

from Curling_League_App.competition import Competition
from Curling_League_App.identified_object import IdentifiedObject
from Curling_League_App.league_database import LeagueDatabase
from Curling_League_App.team import Team
from Curling_League_App.team_member import TeamMember
from Curling_League_App.exceptions.duplicate_oid import DuplicateOid
from Curling_League_App.exceptions.duplicate_email import DuplicateEmail
from Curling_League_App.league import League

import functools
from Curling_League_App.edit_member_dialog import EditMemberDialog





Ui_MainWindow, QtBaseWindow = uic.loadUiType("edit_dialog.ui")

class EditDialog(QtBaseWindow, Ui_MainWindow):
    def __init__(self, selected_league=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.flag = True
        #self.teams = selected_league.teams
        self.edit_dialog_oid = 0

        self.teams = selected_league.teams
        #######################
        self.league = selected_league
        self.add_team_button.clicked.connect(self.addTeam)
        self.delete_team_button.clicked.connect(self.removeTeam)
        self.edit_team_button.clicked.connect(self.editTeam)
        self.export_button.clicked.connect(self.exportTeam)
        self.import_button.clicked.connect(self.importTeam)
        if selected_league:
            #self.teams = selected_league.teams
            self.league_teams_list_widget.clear()
            for team in self.teams:
                #self.league_teams_list_widget.clear()
                for item in self.teams:
                    self.league_teams_list_widget.addItem(str(item))
            self.update_league()

    def addTeam(self):
        add_new_team = QtWidgets.QInputDialog.getText(self, "Add Team", "Enter team name:")
        if add_new_team[1]:
            while (self.flag):
                new_team = Team(self.edit_dialog_oid, add_new_team[0])

                try:
                    self.league.add_team(new_team)
                    self.flag = False
                except:
                    self.oid_fixer()
                    del new_team

            self.update_league()
            self.flag = True


        else:
            print("canceled")

    def removeTeam(self):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Icon.Question)
        dialog.setWindowTitle("Remove Team")
        dialog.setText("Are you sure you want to delete this team from the league?")
        no = dialog.addButton("No", QMessageBox.ButtonRole.RejectRole)
        yes = dialog.addButton("Yes", QMessageBox.ButtonRole.AcceptRole)

        dialog.exec()
        if dialog.clickedButton() == yes:
            del self.teams[self.league_teams_list_widget.currentRow()]
            self.update_league()
        else:
            print("No")






    def editTeam(self):
        row = self.league_teams_list_widget.currentRow()
        selected_team = self.teams[row]
        dialog = EditMemberDialog(selected_team)

        dialog.accepted.connect(functools.partial(self.edit_team_dialog_accepted, dialog, selected_team))
        dialog.show()
        #if dialog.exec() == QDialog.DialogCode.Accepted:
        self.update_league()

    def edit_team_dialog_accepted(self, source, selected_team):
        source.update_league(selected_team)
        self.update_league()



    def update_league(self):
        self.league_teams_list_widget.clear()
        for item in self.teams:
            self.league_teams_list_widget.addItem(str(item))

    def oid_fixer(self):
        self.edit_dialog_oid += 1
        return self.edit_dialog_oid



    def importTeam(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File')
        if fname[0] != "":
            thisn = LeagueDatabase()
            thisn.import_league_teams(self.league, fname[0])
            self.update_league()
        else:
            pass

    def exportTeam(self):
        fname = QFileDialog.getSaveFileName(self, 'Save File')
        if fname[0] != "":
            thisn = LeagueDatabase()
            thisn.export_league_teams(self.league, fname[0])
            self.update_league()
        else:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditDialog()
    window.show()
    sys.exit(app.exec_())