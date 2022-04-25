from PyQt5 import uic, QtWidgets
import sys

from Curling_League_App.competition import Competition
from Curling_League_App.identified_object import IdentifiedObject
from Curling_League_App.league_database import LeagueDatabase
from Curling_League_App.team import Team
from Curling_League_App.team_member import TeamMember
from Curling_League_App.exceptions.duplicate_oid import DuplicateOid
from Curling_League_App.exceptions.duplicate_email import DuplicateEmail
from Curling_League_App.league import League





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
                #self.thisDatabse.next_oid()
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

    def update_league(self):
        self.league_teams_list_widget.clear()
        for item in self.teams:
            self.league_teams_list_widget.addItem(str(item))

    def oid_fixer(self):

        self.edit_dialog_oid += 1
        return self.edit_dialog_oid


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditDialog()
    window.show()
    sys.exit(app.exec_())