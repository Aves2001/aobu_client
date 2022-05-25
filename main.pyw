from os import walk
from os.path import basename, normpath, dirname, isfile
from sys import argv, exit

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidgetItem, QFileDialog
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import parse_site.settings
from ConnectDatabase import ConnectDatabase, params_default
from FormDirBook import FormDirBook
from FormInfoSiteBook import FormInfoSiteBook
from Login import Login
from QMessageBox import warning
from localDB import LocalDB
from parse_site.spiders.BazaKnigGetBook import BazaKnigGetBook
from ui.main_ui import Ui_MainWindow


def get_book_site(urls: list):
    process = CrawlerProcess(get_project_settings())
    process.crawl(BazaKnigGetBook, urls=urls)
    process.start()


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icon/aggregate.png"))
        self.user_id = None
        self.user_login = None

        self.change_visible_btn(False)

        self.ui.pBtn_add_path.clicked.connect(self.add_dir)
        self.ui.pBtn_remove_path.clicked.connect(self.remove_dir)
        self.ui.pBtn_save_curent_path.clicked.connect(self.save_folder_mp3_info)
        self.ui.pBtn_search.clicked.connect(self.search_book)

        self.ui.pBtn_add_site_book.clicked.connect(self.parse_book)

        self.ui.listWidget_site.itemClicked.connect(self.list_widget_site_item_clicked)
        self.ui.listWidget_dir.itemClicked.connect(self.list_widget_dir_item_clicked)
        self.ui.pushButton_add_author.clicked.connect(self.add_author)
        self.ui.toolBox.currentChanged.connect(self.page_change)

    def parse_book(self):
        text = self.ui.textEdit_site_book_link.toPlainText()
        text = text.split()
        self.ui.textEdit_site_book_link.clear()
        if len(text) > 0:
            message = f'Кількість книжок яка буде добавлена в БД: [{len(text)}]\nЯкщо посилання введено коректно'
            warning(message=message, info=True)
            parse_site.settings.SPIDER_URLS = text
            get_book_site(text)

    def search_book(self):
        self.ui.listWidget_site.clear()
        number_failures = 0

        db = LocalDB()
        books = db.get_user_book_info(self.user_id)
        db.close()

        con = ConnectDatabase(*params_default)
        if con.connect is not None:
            for book in books:
                book = list(book)
                for i, j in enumerate(book):
                    if len(j) == 0:
                        book[i] = None
                try:
                    id_book = con.search_id_book(book[0], book[1], book[2], book[3])[0]
                    id_book = id_book['id_book']
                    book_site = con.select_book(id_book)

                    it = QListWidgetItem()
                    it.setText(book_site['genres'][0]['name'])
                    it.setData(1, book_site)
                    self.ui.listWidget_site.addItem(it)
                except:
                    number_failures += 1
            if number_failures > 0:
                found = len(books) - number_failures
                warning(message=f'Кількість знайдених книжок: [{found}/{len(books)}]', info=True)
            else:
                warning(message=f'Кількість знайдених книжок: [{len(books)}]')
        else:
            return

    def clear_layout(self, layout=None):
        if layout is None:
            layout = self.ui.verticalLayout_dir

        for i in reversed(range(layout.count())):
            layout_item = layout.itemAt(i)
            if layout_item.widget() is not None:
                widget_to_remove = layout_item.widget()
                widget_to_remove.setParent(None)
                layout.removeWidget(widget_to_remove)
            elif layout_item.spacerItem() is not None:
                print("found spacer: " + str(layout_item.spacerItem()))
            else:
                layout_to_remove = layout.itemAt(i)
                self.clear_layout(layout_to_remove)

    def change_visible_btn(self, visible: bool):
        if visible:
            self.ui.pBtn_add_path.show()
            self.ui.pBtn_remove_path.show()
            self.ui.pBtn_save_curent_path.show()
            self.ui.pBtn_search.hide()
        else:
            self.ui.pBtn_search.show()
            self.ui.pBtn_add_path.hide()
            self.ui.pBtn_remove_path.hide()
            self.ui.pBtn_save_curent_path.hide()

    def page_change(self):
        if self.ui.site.isVisible():
            self.ui.stackedWidget.setCurrentIndex(0)
            self.change_visible_btn(False)
        elif self.ui.dir.isVisible():
            self.ui.stackedWidget.setCurrentIndex(1)
            self.change_visible_btn(True)

    def list_widget_site_item_clicked(self):
        data = self.ui.listWidget_site.currentItem().data(1)
        self.clear_layout(self.ui.verticalLayout_FormInfoSiteBook)
        self.ui.verticalLayout_FormInfoSiteBook.addWidget(FormInfoSiteBook(data))

    def list_widget_dir_item_clicked(self):
        id_folder = self.ui.listWidget_dir.currentItem().data(1)[0]

        db = LocalDB()
        dir_book = db.get_book(id_folder)
        authors = db.get_authors()
        db.close()

        self.clear_layout(self.ui.verticalLayout_dir)
        for book in dir_book:
            if book[2] is None:
                title = basename(
                    dirname(book[0])
                )
            else:
                title = book[2]

            if book[1] is None:
                current_id_author = None
            else:
                current_id_author = book[1]
            self.ui.verticalLayout_dir.addWidget(
                FormDirBook(title=title,
                            path=book[0],
                            authors_items=authors,
                            current_id_author=current_id_author
                            ))

    def save_folder_mp3_info(self):
        if self.ui.listWidget_dir.currentItem() is None:
            warning(message="Спочатку виберіть папку")
            return
        db = LocalDB()

        layout = self.ui.verticalLayout_dir
        for i in range(layout.count()):
            layout_item = layout.itemAt(i)
            if layout_item.widget() is not None:
                widget: FormDirBook = layout_item.widget()

                title = widget.ui.lineEdit_title_book.text()
                author_id = widget.ui.comboBox_authors.currentData()
                path = widget.path
                if author_id == -1:
                    author_id = None
                if title == basename(dirname(path)):
                    title = None
                db.save_folder_mp3_info(path=path, title=title, author_id=author_id)
        db.close()
        current_item = self.ui.listWidget_dir.currentItem().text()
        warning(message="Дані збережено", title=current_item, info=True)

    def successfully_login(self, id_user, login):
        self.user_id = id_user
        self.user_login = login
        self.ui.qlabel_user_login.setText(login)
        self.ui.qlabel_user_login.adjustSize()
        self.get_dir()

    def get_dir(self):
        try:
            db = LocalDB()
            dir = db.get_dir(self.user_id)
            db.close()

            for item in dir:
                it = QListWidgetItem()
                it.setText(item[0])
                it.setData(1, [item[1], item[2]])
                self.ui.listWidget_dir.addItem(it)
        except Exception as e:
            warning(message=str(e))

    def add_dir(self):
        dir_full_path: str = QFileDialog.getExistingDirectory(self, "Вибрати папку", ".")
        dir_full_path = normpath(dir_full_path)
        dir_basename: str = basename(dir_full_path)

        try:
            for root, dirs, files in walk(dir_full_path):
                for file in files:
                    if file.endswith(".mp3"):
                        raise Exception
            warning(message="Аудіо файли не знайдені")
            return
        except:
            pass

        db = LocalDB()
        db.add_dir(self.user_id, dir_basename, dir_full_path)
        db.close()
        self.ui.listWidget_dir.clear()
        self.get_dir()

    def remove_dir(self):
        if self.ui.listWidget_dir.currentItem() is None:
            warning(message="Спочатку виберіть папку")
            return
        item = self.ui.listWidget_dir.currentItem()
        id_folder = item.data(1)[0]

        db = LocalDB()
        db.remove_book_user(id_user=self.user_id, id_folder=id_folder)
        db.close()
        self.clear_layout()
        self.ui.listWidget_dir.clear()
        self.get_dir()

    def add_author(self):
        surname = self.ui.lineEdit_a_surname.text()
        name = self.ui.lineEdit_a_name.text()
        nick = self.ui.lineEdit_a_nick.text()

        for _ in range(1):
            if len(surname) == 0 and len(name) == 0 and len(nick) == 0:
                warning(message="Спочатку введіть дані")
                return

            if len(surname) == 0 and len(name) == 0:
                if len(nick) < 3:
                    warning(message="Ви ввели занадто короткий нікнейм автора")
                    return
                else:
                    break

            if len(surname) < 3:
                warning(message="Ви ввели занадто коротке прізвище автора")
                return
            if len(name) < 3:
                warning(message="Ви ввели занадто коротке ім'я автора")
                return

        db = LocalDB()
        db.add_author(surname=surname, name=name, nick=nick)
        db.close()

        self.ui.lineEdit_a_surname.clear()
        self.ui.lineEdit_a_name.clear()
        self.ui.lineEdit_a_nick.clear()

        is_selected_item = len(self.ui.listWidget_dir.selectedIndexes()) > 0
        if is_selected_item:
            self.update_combobox(surname, name, nick)

    def update_combobox(self, surname, name, nick, layout=None):
        if layout is None:
            layout = self.ui.verticalLayout_dir
        db = LocalDB()
        authors = db.get_authors()
        db.close()

        tmp = list()
        for i in authors:
            tmp.append(list(i)[1:])

        index = tmp.index([surname, name, nick])
        text = ' '.join(tmp.pop(index)).strip()
        data = authors[index][0]

        for i in range(layout.count()):
            layout_item = layout.itemAt(i)
            if layout_item.widget() is not None:
                widget: FormDirBook = layout_item.widget()
                if widget.ui.comboBox_authors.findData(data) == -1:
                    widget.ui.comboBox_authors.addItem(text, data)


def app():
    application = QtWidgets.QApplication(argv)
    if not isfile("database.db"):
        warning(message="Зачекайте, будь ласка, створюється база даних", title="Перший запуск", info=True)

    # application.setStyleSheet(open("dark-theme.stylesheet").read())
    main = Main()
    # вхід
    Login(main)

    exit(application.exec_())


if __name__ == "__main__":
    app()

