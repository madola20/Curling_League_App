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
        self.edit_member_oid = 0
        self.member_flag = True
        self.team = selected_team

        self.members = selected_team.members

        self.add_member_button.clicked.connect(self.addMember)



    def addMember(self):


        while (self.member_flag):
            new_member = TeamMember(self.edit_member_oid, self.name_line.text(), self.email_line.text())

            try:
                self.team.add_member(new_member)
                self.member_flag = False
            except DuplicateOid:
                self.member_oid_fixer()
                del new_member

            except DuplicateEmail:
                del new_member
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Duplicate Email")
                msg.setInformativeText('That email already exists!\nProvide unique email.')
                msg.setWindowTitle("Error")
                msg.exec_()
                break



        self.name_line.setText("")
        self.email_line.setText("")
        self.update_team()
        self.member_flag = True



    def update_team(self):
        self.member_list_widget.clear()
        for item in self.members:
            self.member_list_widget.addItem(str(item))

    def member_oid_fixer(self):
        self.edit_member_oid += 1
        return self.edit_member_oid

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditMemberDialog()
    window.show()
    sys.exit(app.exec_())