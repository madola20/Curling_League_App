from PyQt5 import uic, QtWidgets
import sys

from PyQt5.QtWidgets import QMessageBox

from Curling_League_App.competition import Competition
from Curling_League_App.identified_object import IdentifiedObject
from Curling_League_App.league_database import LeagueDatabase
from Curling_League_App.team import Team
from Curling_League_App.team_member import TeamMember
from Curling_League_App.exceptions.duplicate_oid import DuplicateOid
from Curling_League_App.exceptions.duplicate_email import DuplicateEmail
from Curling_League_App.league import League

Ui_MainWindow, QtBaseWindow = uic.loadUiType("edit_member_dialog.ui")

class EditMemberDialog(QtBaseWindow, Ui_MainWindow):
    def __init__(self, selected_team=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.members = selected_team.members












if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditMemberDialog()
    window.show()
    sys.exit(app.exec_())