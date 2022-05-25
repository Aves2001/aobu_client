from typing import Dict, Any

import pymysql
import pymysql.cursors

from QMessageBox import warning
from gensql import gen_fill_sql_add_book, gen_INSERT_SET

params_default = [
    "127.0.0.1",
    "root",
    "",
    "aobu"
]


class ConnectDatabase:
    def __init__(self, host: str, user: str, password: str, db_name: str):
        self.title = f'Підключення до бази даних [{db_name}]'
        self.connect = None
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name

        self.connect_init()

    def connect_init(self):
        try:
            self.connect = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name,
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            warning(exception=e, title=self.title)
            return

    def login(self, login: str, password: str):
        id_user = -1
        try:
            with self.connect.cursor() as cursor:
                cursor.execute("SELECT `id_user` FROM `users` WHERE `login` = %s AND `password` = %s",
                               [login, password])
                try:
                    id_user: int = cursor.fetchall()[0]['id_user']
                except:
                    id_user = -1

                if id_user != -1:
                    cursor.execute("START TRANSACTION;")
                    cursor.execute("""
                    UPDATE `users`
                        SET `last_login_date`= CURRENT_TIMESTAMP
                        WHERE `login` = %s AND `password` = %s
                    """, [login, password])

                    cursor.execute("COMMIT;")
        except Exception as e:
            warning(exception=e, title=self.title)
        finally:
            return id_user

    def registration(self, name: str, login: str, password: str) -> int:
        id_user = -1
        try:
            with self.connect.cursor() as cursor:
                cursor.execute("START TRANSACTION;")
                cursor.execute("INSERT INTO `users` (`name`, `Login`, `password`) VALUES (%s, %s, %s)",
                               [name, login, password])
                cursor.execute("COMMIT;")

                cursor.execute("""
                SELECT `id_user`
                FROM `users`
                WHERE `login` = %s AND `password` = %s
                """, [login, password])

                try:
                    id_user: int = cursor.fetchall()[0]['id_user']
                except:
                    id_user = -1
        except Exception as e:
            warning(exception=e, title=self.title)
        finally:
            return id_user

    def add_book(self, item) -> None:
        try:
            sql_set, value_set = gen_INSERT_SET(item)
            sql_add_book = gen_fill_sql_add_book(item)

            with self.connect.cursor() as cursor:
                cursor.execute("START TRANSACTION;")
                for i in range(len(sql_set)):
                    cursor.execute(sql_set[i], value_set[i])

                for i in sql_add_book:
                    cursor.execute(i)

                cursor.execute("COMMIT;")
        except Exception as e:
            if e.args[0] == 1062:
                return
            warning(exception=e, title=self.title)

    def select_book(self, id_book) -> Dict[str, Any]:
        book = dict()
        try:
            with self.connect.cursor() as cursor:
                sql = """
    SELECT books_from_websites.id_book, book_title.book_title, books_from_websites.image, 
    books_year.year, books_duration.duration, books_price.price, books_rating.rating,
    books_from_websites.brief_content, books_from_websites.is_audio, books_from_websites.link, books_from_websites.info_update_date
        FROM books_from_websites
        LEFT JOIN book_title
            ON books_from_websites.book_title = book_title.id_book_title
        LEFT JOIN books_year
            ON books_from_websites.id_book = books_year.id_book
        LEFT JOIN books_duration
            ON books_from_websites.id_book = books_duration.id_book
        LEFT JOIN books_price
            ON books_from_websites.id_book = books_price.id_book
        LEFT JOIN books_rating
            ON books_from_websites.id_book = books_rating.id_book
        WHERE books_from_websites.id_book = %s
"""
                cursor.execute(sql, id_book)

                book.update(cursor.fetchall()[0])
        #############################################################################
                cursor.execute("""
                SELECT authors.surname, authors.name, authors.nickname
                FROM books_authors
                LEFT JOIN authors
                    ON books_authors.id_author = authors.id_author
                WHERE books_authors.id_book = %s
                """, id_book)

                authors = cursor.fetchall()
                book.update({
                    'authors': authors
                })
                #############################################################################
                cursor.execute("""
                SELECT readers.surname, readers.name, readers.nickname
                    FROM books_readers
                    LEFT JOIN readers
                        ON books_readers.id_reader = readers.id_reader
                    WHERE books_readers.id_book = %s
                """, id_book)
                readers = cursor.fetchall()
                book.update({
                    'readers': readers
                })
                ######
                cursor.execute("""
                SELECT sites.name, sites_genres.genre
                    FROM books_genres
                    LEFT JOIN `sites_genres`
                        ON books_genres.id_genre = sites_genres.id_genre
                    LEFT JOIN sites
                        ON sites_genres.id_site = sites.id_site
                    WHERE books_genres.id_book = %s
                """, id_book)
                genres = cursor.fetchall()
                book.update({
                    'genres': genres
                })
                return book

        except Exception as e:
            warning(exception=e, title=self.title)

    def search_id_book(self, title: str, surname, name, nick):
        try:
            with self.connect.cursor() as cursor:
                sql = """
            SELECT books_authors.id_book
                FROM authors
                LEFT JOIN books_authors
                    ON authors.id_author = books_authors.id_author
                LEFT JOIN book_title
                    ON books_authors.id_book = book_title.id_book_title
"""
                if title is not None:
                    if surname is not None and name is not None and nick is None:
                        sql = f"""{sql}
                            WHERE book_title.book_title = %s AND authors.surname = %s and authors.name = %s
                        """
                        cursor.execute(sql, [title, surname, name])
                        return cursor.fetchall()
                    elif surname is None and name is None and nick is not None:
                        sql = f"""{sql}
                            WHERE book_title.book_title = %s AND authors.nickname = %s 
                        """
                        cursor.execute(sql, [title, nick])
                        return cursor.fetchall()
                else:
                    return

        except Exception as e:
            warning(exception=e, title=self.title)

    def close(self):
        self.connect.close()
