from PyQt5.QtWidgets import QWidget

from ui.info_dir import Ui_Form


class FormDirBook(QWidget):
    def __init__(self, title, path, authors_items, current_id_author):
        super(FormDirBook, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.lineEdit_title_book.setText(title)
        self.path = path
        self.ui.lineEdit_path.setText(path)

        self.ui.comboBox_authors.addItem("Не вибрано", -1)

        for a in authors_items:
            id_authors = a[0]
            a = a[1:]
            a = " ".join(a).strip()
            self.ui.comboBox_authors.addItem(a, id_authors)

        if current_id_author is not None:
            index = self.ui.comboBox_authors.findData(current_id_author)
            self.ui.comboBox_authors.setCurrentIndex(index)
