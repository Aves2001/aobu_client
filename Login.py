from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from ConnectDatabase import ConnectDatabase, params_default
from QMessageBox import warning
from Registration import Registration
from localDB import LocalDB
from ui.login import Ui_DialogLogin


class Login(QtWidgets.QDialog):
    def __init__(self, main):
        super(Login, self).__init__()
        self.registration = None
        self.main = main
        self.ui = Ui_DialogLogin()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icon/aggregate.png"))

        self.ui.checkBox_view_password.clicked.connect(self.view_password)
        self.ui.pushButton_entry.clicked.connect(self.entry_clicked)
        self.ui.label_register.mousePressEvent = self.show_registration

        self.save_login()
        self.ui.comboBox_save_password.currentIndexChanged[str].connect(self.set_login_password)

        self.show()

    def view_password(self):
        if self.ui.checkBox_view_password.isChecked():
            self.ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def entry_clicked(self) -> None:
        login = self.ui.lineEdit_login.text()
        password = self.ui.lineEdit_password.text()

        if len(login) == 0:
            warning(message="Ви не ввели логін")
            return

        if len(login) < 4:
            warning(message="Логін має буди більше 4 символів")
            return

        if len(password) == 0:
            warning(message="Ви не ввели пароль")
            return

        if len(password) < 4:
            warning(message="Пароль має будти більше 4 символів")
            return

        con = ConnectDatabase(*params_default)
        if con.connect is not None:
            id_user = con.login(login=login, password=password)
            successfully_login = id_user > 0
        else:
            return

        if successfully_login:
            self.save_user(id_user=id_user, login=login, password=password)

            self.main.successfully_login(id_user=id_user, login=login)

            self.main.show()
            if self.registration is not None:
                self.registration.close()
            self.close()
        else:
            warning(message="Не вірно введено логін або пароль")

    def set_login_password(self):
        login = self.ui.comboBox_save_password.currentText()
        password = self.ui.comboBox_save_password.currentData()
        self.ui.lineEdit_login.setText(login)
        self.ui.lineEdit_password.setText(password)

    def save_login(self):
        try:
            con = LocalDB()
            data = con.save_login()

            if len(data) == 0:
                self.ui.comboBox_save_password.hide()
                return
            for item in data:
                self.ui.comboBox_save_password.addItem(item[0], item[1])
            con.close()
            self.set_login_password()
        except:
            self.ui.lineEdit_login.setText('')
            self.ui.lineEdit_password.setText('')

    def show_registration(self, _):
        if self.registration is None:
            self.registration = Registration(self)
        self.registration.show()
        self.hide()

    def save_user(self, id_user, login="", password=""):
        local_db = LocalDB()
        if self.ui.checkBox_save_password.isChecked():
            local_db.add_user(id_user=id_user, login=login, password=password)
        else:
            is_no_user = local_db.is_no_user(id_user)
            if is_no_user:
                local_db.add_user(id_user=id_user)
        local_db.close()
