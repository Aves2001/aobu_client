from os.path import isfile

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel

from ui.info_site_book import Ui_Form
from httplib2 import Http


class FormInfoSiteBook(QWidget):
    def __init__(self, item: dict):
        super(FormInfoSiteBook, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_img.setScaledContents(True)

        title = item['book_title']
        image_link = item['image']
        authors = item['authors']
        readers = item['readers']
        year = str(item['year'])
        duration = str(item['duration'])
        genres = item['genres']

        self.ui.label_title.setText(title)
        self.add_image(image_link)
        self.add_authors(authors)
        self.add_readers(readers)
        self.ui.label_year.setText(year)
        self.ui.label_duration.setText(duration)
        self.add_genres(genres)

    def add_image(self, image_link: str):
        file_name = image_link.split('/')[-1]
        path_file = f'.cache/{file_name}'

        if not isfile(path_file):
            h = Http('.cache')
            response, content = h.request(image_link)
            out = open(path_file, 'wb')
            out.write(content)
            out.close()
        pixmap = QPixmap(path_file)
        pixmap.scaled(300,200)
        self.ui.label_img.setPixmap(pixmap)

    def add_authors(self, authors):
        for author in authors:
            if author['nickname'] is None or len(author['nickname']) == 0:
                l_author = " ".join([author['surname'], author['name']])
            else:
                l_author = author['nickname']
            label_a = QLabel(self)
            label_a.setText(l_author)
            self.ui.horizontalLayout_authors.addWidget(label_a)

    def add_readers(self, readers):
        for reader in readers:
            if reader['nickname'] is None or len(reader['nickname']) == 0:
                l_reader = " ".join([reader['surname'], reader['name']])
            else:
                l_reader = reader['nickname']
            label_r = QLabel(self)
            label_r.setText(l_reader)
            self.ui.horizontalLayout_readers.addWidget(label_r)

    def add_genres(self, genres):
        for i, genre in enumerate(genres):
            if genre['genre'] is None or len(genre['genre']) != 0:
                genre = genre['genre']
            label = QLabel(self)
            label.setText(genre)

            self.ui.horizontalLayout_genres.addWidget(label)
            if i != len(genres)-1:
                label_1 = QLabel(self)
                label_1.setText('/')
                self.ui.horizontalLayout_genres.addWidget(label_1)

