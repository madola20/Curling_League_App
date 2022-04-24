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
        self.teams = selected_league.teams
        if selected_league:
            self.league_teams_list_widget.clear()
            for team in self.teams:
                #self.league_teams_list_widget.clear()
                for item in self.teams:
                    self.league_teams_list_widget.addItem(str(item))


    def update_league(self):
        pass
        #selected_league.


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditDialog()
    window.show()
    sys.exit(app.exec_())