from PyQt5.QtGui import QIcon
from ConnectDatabase import ConnectDatabase, params_default
from QMessageBox import warning
from localDB import LocalDB
from ui.registration import Ui_DialogRegistration
from PyQt5 import QtWidgets


class Registration(QtWidgets.QDialog):
    def __init__(self, login):
        super(Registration, self).__init__()
        self.login = login
        self.ui = Ui_DialogRegistration()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icon/aggregate.png"))

        self.ui.checkBox_view_password.clicked.connect(self.view_password)
        self.ui.pushButton_reg.clicked.connect(self.reg_clicked)
        self.ui.label_log_in.mousePressEvent = self.show_login

    def view_password(self):
        if self.ui.checkBox_view_password.isChecked():
            self.ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.lineEdit_password_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.lineEdit_password_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def reg_clicked(self) -> None:
        name = self.ui.lineEdit_user_name.text()
        login = self.ui.lineEdit_login.text()
        password = self.ui.lineEdit_password.text()
        password2 = self.ui.lineEdit_password_2.text()

        # todo
        if len(login) == 0:
            warning(message="Ви не ввели логін")
            return

        if len(login) < 4:
            warning(message="Логін має буди більше 4 символів")
            return

        if len(password) == 0 and len(password2) == 0:
            warning(message="Ви не ввели пароль")
            return

        if len(password) == 0 or len(password2) == 0:
            warning(message="Підтвердіть введений пароль")
            return

        if password != password2:
            warning(message="Введені паролі не збігаюсться")
            return

        if len(password) < 4:
            warning(message="Пароль має будти більше 4 символів")
            return

        con = ConnectDatabase(*params_default)
        if con.connect is not None:
            id_user = con.registration(name=name, login=login, password=password)
            successfully_registration = id_user > 0
        else:
            return

        if successfully_registration:
            self.save_user(id_user, login, password)
            self.login.main.successfully_login(id_user=id_user, login=login)
            if self.login is not None:
                self.login.main.show()
                self.login.close()
            self.close()

    def save_user(self, id_user, login="", password=""):
        local_db = LocalDB()
        if self.ui.checkBox_save_password.isChecked():
            local_db.add_user(id_user=id_user, login=login, password=password)
        else:
            is_no_user = local_db.is_no_user(id_user)
            if is_no_user:
                local_db.add_user(id_user=id_user)
        local_db.close()

    def show_login(self, _):
        self.login.show()
        self.hide()
