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

        self.delete_member_button.clicked.connect(self.removeMember)
        self.add_member_button.clicked.connect(self.addMember)
        self.edit_member_button.clicked.connect(self.updateMemeber)

        if selected_team:
            #self.teams = selected_league.teams
            self.member_list_widget.clear()
            for member in self.members:

                self.member_list_widget.addItem(str(member))
            self.update_team()



    def addMember(self):
        while (self.member_flag):
            new_member = TeamMember(self.edit_member_oid, self.name_line.text(), self.email_line.text())
            try:
                #self.team.add_member(new_member)
                #self.member_flag = False
                if (self.name_line.text() == "" or self.email_line.text() == ""):
                    del new_member
                    msg1 = QMessageBox()
                    msg1.setIcon(QMessageBox.Critical)
                    msg1.setText("Invalid Response")
                    msg1.setInformativeText('Nothing was entered!\nProvide name and email.')
                    msg1.setWindowTitle("Error")
                    msg1.exec_()
                    break
                else:
                    self.team.add_member(new_member)
                    self.member_flag = False
            except DuplicateOid:
                self.member_oid_fixer()
                del new_member

            except DuplicateEmail:
                del new_member
                msg2 = QMessageBox()
                msg2.setIcon(QMessageBox.Critical)
                msg2.setText("Duplicate Email")
                msg2.setInformativeText('That email already exists!\nProvide unique email.')
                msg2.setWindowTitle("Error")
                msg2.exec_()
                break

        self.name_line.setText("")
        self.email_line.setText("")
        self.update_team()

        self.member_flag = True


    def updateMemeber(self):
        updating_member = self.members[self.member_list_widget.currentRow()]
        if (self.name_line.text() != ""):
            updating_member._name = self.name_line.text()
            #updating_member._email = self.email_line.text()
        if (self.email_line.text() != ""):
            updating_member._email = self.email_line.text()
        if (self.email_line.text() == ""):
            pass
        if (self.name_line.text() != ""):
            pass
        else:
            pass



        self.name_line.setText("")
        self.email_line.setText("")
        self.update_team()

    def removeMember(self):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Icon.Question)
        dialog.setWindowTitle("Remove Member")
        dialog.setText("Are you sure you want to delete this member from the team?")
        no = dialog.addButton("No", QMessageBox.ButtonRole.RejectRole)
        yes = dialog.addButton("Yes", QMessageBox.ButtonRole.AcceptRole)

        dialog.exec()
        if dialog.clickedButton() == yes:
            del self.members[self.member_list_widget.currentRow()]
            self.update_team()
        else:
            print("No")

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