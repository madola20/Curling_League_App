from PyQt5 import uic, QtWidgets
import sys





Ui_MainWindow, QtBaseWindow = uic.loadUiType("edit_dialog.ui")

class EditDialog(QtBaseWindow, Ui_MainWindow):
    def __init__(self, selected_league=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        if selected_league:
            pass

    def update_league(self):
        pass
        #selected_league.


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditDialog()
    window.show()
    sys.exit(app.exec_())