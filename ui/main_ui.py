# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 525)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(900, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.qlabel_user_login = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.qlabel_user_login.setFont(font)
        self.qlabel_user_login.setText("")
        self.qlabel_user_login.setObjectName("qlabel_user_login")
        self.horizontalLayout_3.addWidget(self.qlabel_user_login)
        spacerItem2 = QtWidgets.QSpacerItem(900, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setMinimumSize(QtCore.QSize(250, 200))
        self.toolBox.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolBox.setFont(font)
        self.toolBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolBox.setFrameShape(QtWidgets.QFrame.Box)
        self.toolBox.setObjectName("toolBox")
        self.site = QtWidgets.QWidget()
        self.site.setGeometry(QtCore.QRect(0, 0, 248, 370))
        self.site.setObjectName("site")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.site)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget_site = QtWidgets.QListWidget(self.site)
        self.listWidget_site.setObjectName("listWidget_site")
        self.verticalLayout.addWidget(self.listWidget_site)
        self.toolBox.addItem(self.site, "")
        self.dir = QtWidgets.QWidget()
        self.dir.setGeometry(QtCore.QRect(0, 0, 248, 370))
        self.dir.setObjectName("dir")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dir)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget_dir = QtWidgets.QListWidget(self.dir)
        self.listWidget_dir.setObjectName("listWidget_dir")
        self.verticalLayout_2.addWidget(self.listWidget_dir)
        self.toolBox.addItem(self.dir, "")
        self.horizontalLayout_4.addWidget(self.toolBox)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_site = QtWidgets.QWidget()
        self.page_site.setObjectName("page_site")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_site)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.page_site)
        self.label_2.setMinimumSize(QtCore.QSize(380, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setLineWidth(2)
        self.label_2.setMidLineWidth(2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_site)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 378, 361))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_FormInfoSiteBook = QtWidgets.QVBoxLayout()
        self.verticalLayout_FormInfoSiteBook.setObjectName("verticalLayout_FormInfoSiteBook")
        self.verticalLayout_10.addLayout(self.verticalLayout_FormInfoSiteBook)
        spacerItem5 = QtWidgets.QSpacerItem(170, 332, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_7.addWidget(self.scrollArea_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        spacerItem6 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.page_site)
        self.label.setMaximumSize(QtCore.QSize(330, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(2)
        self.label.setMidLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.textEdit_site_book_link = QtWidgets.QTextEdit(self.page_site)
        self.textEdit_site_book_link.setMaximumSize(QtCore.QSize(330, 16777215))
        self.textEdit_site_book_link.setObjectName("textEdit_site_book_link")
        self.verticalLayout_6.addWidget(self.textEdit_site_book_link)
        self.pBtn_add_site_book = QtWidgets.QPushButton(self.page_site)
        self.pBtn_add_site_book.setMaximumSize(QtCore.QSize(330, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pBtn_add_site_book.setFont(font)
        self.pBtn_add_site_book.setObjectName("pBtn_add_site_book")
        self.verticalLayout_6.addWidget(self.pBtn_add_site_book)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.stackedWidget.addWidget(self.page_site)
        self.page_dir = QtWidgets.QWidget()
        self.page_dir.setObjectName("page_dir")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_dir)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.page_dir)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setLineWidth(2)
        self.label_5.setMidLineWidth(2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.scrollArea = QtWidgets.QScrollArea(self.page_dir)
        self.scrollArea.setMinimumSize(QtCore.QSize(320, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 318, 28))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_dir = QtWidgets.QVBoxLayout()
        self.verticalLayout_dir.setObjectName("verticalLayout_dir")
        self.verticalLayout_8.addLayout(self.verticalLayout_dir)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.page_dir)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setLineWidth(2)
        self.label_4.setMidLineWidth(2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.frame = QtWidgets.QFrame(self.page_dir)
        self.frame.setMinimumSize(QtCore.QSize(20, 20))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(5)
        self.frame.setObjectName("frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lineEdit_a_surname = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_a_surname.setFont(font)
        self.lineEdit_a_surname.setObjectName("lineEdit_a_surname")
        self.verticalLayout_9.addWidget(self.lineEdit_a_surname)
        self.lineEdit_a_name = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_a_name.setObjectName("lineEdit_a_name")
        self.verticalLayout_9.addWidget(self.lineEdit_a_name)
        self.lineEdit_a_nick = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_a_nick.setObjectName("lineEdit_a_nick")
        self.verticalLayout_9.addWidget(self.lineEdit_a_nick)
        self.pushButton_add_author = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add_author.setFont(font)
        self.pushButton_add_author.setObjectName("pushButton_add_author")
        self.verticalLayout_9.addWidget(self.pushButton_add_author)
        self.verticalLayout_3.addWidget(self.frame)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.page_dir)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_btn_dir = QtWidgets.QHBoxLayout()
        self.horizontalLayout_btn_dir.setObjectName("horizontalLayout_btn_dir")
        self.pBtn_add_path = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pBtn_add_path.setFont(font)
        self.pBtn_add_path.setObjectName("pBtn_add_path")
        self.horizontalLayout_btn_dir.addWidget(self.pBtn_add_path)
        self.pBtn_remove_path = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pBtn_remove_path.setFont(font)
        self.pBtn_remove_path.setObjectName("pBtn_remove_path")
        self.horizontalLayout_btn_dir.addWidget(self.pBtn_remove_path)
        self.pBtn_save_curent_path = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pBtn_save_curent_path.setFont(font)
        self.pBtn_save_curent_path.setObjectName("pBtn_save_curent_path")
        self.horizontalLayout_btn_dir.addWidget(self.pBtn_save_curent_path)
        self.pBtn_search = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pBtn_search.setFont(font)
        self.pBtn_search.setObjectName("pBtn_search")
        self.horizontalLayout_btn_dir.addWidget(self.pBtn_search)
        self.verticalLayout_4.addLayout(self.horizontalLayout_btn_dir)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.layout().setSpacing(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Агрегатор оновлень книжкових інтернет-магазинів"))
        self.label_3.setText(_translate("MainWindow", "Ви увійшли як:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.site), _translate("MainWindow", "Сайти"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.dir), _translate("MainWindow", "Папки"))
        self.label_2.setText(_translate("MainWindow", "Книжки на сайті"))
        self.label.setText(_translate("MainWindow", "Список посилань на відсутні в базі книжки"))
        self.pBtn_add_site_book.setText(_translate("MainWindow", "Додати відсутні книжки"))
        self.label_5.setText(_translate("MainWindow", "Список книжок в папці"))
        self.label_4.setText(_translate("MainWindow", "Додавання авторів"))
        self.lineEdit_a_surname.setPlaceholderText(_translate("MainWindow", "Прізвище"))
        self.lineEdit_a_name.setPlaceholderText(_translate("MainWindow", "Ім\'я"))
        self.lineEdit_a_nick.setPlaceholderText(_translate("MainWindow", "Нікнейм"))
        self.pushButton_add_author.setText(_translate("MainWindow", "Додати автора"))
        self.pBtn_add_path.setText(_translate("MainWindow", "Дабавити папку"))
        self.pBtn_remove_path.setText(_translate("MainWindow", "Видалити папку"))
        self.pBtn_save_curent_path.setText(_translate("MainWindow", "Зберегти для цієї папки"))
        self.pBtn_search.setText(_translate("MainWindow", "Пошук"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
