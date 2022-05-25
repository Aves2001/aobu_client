import sqlite3
from os import walk
from os.path import join
from QMessageBox import warning


class LocalDB:
    def __init__(self):
        self._con = sqlite3.connect('database.db')
        self._create_tables()

    def _create_tables(self):
        cur = self._con.cursor()
        sql = """
    PRAGMA foreign_keys = ON;
    
    CREATE TABLE IF NOT EXISTS "users" (
        "id_user"	INTEGER NOT NULL,
        "login"	VARCHAR(30) NOT NULL,
        "password"	VARCHAR(60) NOT NULL,
        PRIMARY KEY("id_user" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "user_folders" (
        "id_user"	INTEGER NOT NULL,
        "id_folder"	INTEGER NOT NULL,
        FOREIGN KEY("id_folder") REFERENCES "folders"("id_folder") ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY("id_user") REFERENCES "users"("id_user") ON DELETE CASCADE ON UPDATE CASCADE
    );
    CREATE TABLE IF NOT EXISTS "folders" (
        "id_folder"	INTEGER NOT NULL,
        "folder_name"	TEXT NOT NULL,
        "path"	TEXT NOT NULL UNIQUE,
        PRIMARY KEY("id_folder" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "authors" (
        "id_author"	INTEGER NOT NULL,
        "surname"	TEXT DEFAULT ' ',
        "name"	TEXT DEFAULT ' ',
        "nick"	TEXT DEFAULT ' ',
        PRIMARY KEY("id_author" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "folders_mp3" (
        "id_folder_mp3"	INTEGER,
        "id_folder"	INTEGER NOT NULL,
        "mp3"	TEXT NOT NULL,
        "id_author"	INTEGER,
        "title"	TEXT,
        PRIMARY KEY("id_folder_mp3" AUTOINCREMENT),
        FOREIGN KEY("id_author") REFERENCES "authors"("id_author") ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY("id_folder") REFERENCES "folders"("id_folder") ON DELETE CASCADE ON UPDATE CASCADE
    );
    CREATE UNIQUE INDEX IF NOT EXISTS "index_user_folders" ON "user_folders" (
        "id_user",
        "id_folder"
    );
    CREATE UNIQUE INDEX IF NOT EXISTS "index_authors" ON "authors" (
        "surname",
        "name",
        "nick"
    );
    CREATE UNIQUE INDEX IF NOT EXISTS "index_mp3" ON "folders_mp3" (
        "mp3"
    );
"""
        for string in sql.split(';'):
            cur.execute(string)
        self._con.commit()

    def is_no_user(self, id_user) -> bool:
        cur = self._con.cursor()
        cur.execute("""
        SELECT id_user
            FROM "users"
            WHERE id_user = ? 
            """, (id_user,))
        return cur.fetchone() == id_user

    def add_user(self, id_user, login="", password="") -> None:
        cur = self._con.cursor()
        try:
            cur.execute(f"""
                        INSERT INTO `users`(`id_user`, `login`, `password`)
                        VALUES
                        (?, ?, ?)
                        """, (id_user, login.strip(), password))
            self._con.commit()
        except:
            cur.execute(f"""
                        UPDATE `users`
                        SET `login`= ?,`password`= ? WHERE `id_user` = ?
                        """, (login.strip(), password, id_user))
            self._con.commit()

    def save_login(self) -> list:
        cur = self._con.cursor()
        cur.execute("""
                SELECT `login`, `password` FROM `users`
                """)
        data = cur.fetchall()

        try:
            while True:
                data.remove(('', ''))
        except:
            pass

        return data

    def add_dir(self, user_id: int, dir_basename: str, dir_full_path: str) -> None:
        cur = self._con.cursor()
        cur.execute("""
            INSERT OR IGNORE
                INTO "folders" ("folder_name", "path")
                VALUES (?, ?);
                """, (dir_basename.strip(), dir_full_path.strip()))

        cur.execute("""
            SELECT "id_folder"
                FROM "folders"
                WHERE "path" = ?
                """, (dir_full_path,))

        id_folder: int = cur.fetchone()[0]

        cur.execute("""
            INSERT OR IGNORE
                INTO "user_folders" ("id_user", "id_folder")
                VALUES (?, ?);
        """, (user_id, id_folder))

        for root, dirs, files in walk(dir_full_path):
            for file in files:
                if file.endswith(".mp3"):
                    cur.execute("""
                    INSERT OR IGNORE
                        INTO "folders_mp3" ("id_folder", "mp3")
                        VALUES (?, ?);
                    """, (id_folder, join(root, file)))
                    break

        self._con.commit()

    def get_dir(self, id_user: int) -> list:
        cur = self._con.cursor()
        cur.execute("""
            SELECT "folder_name", "id_folder", "path"
                FROM "folders"
                WHERE id_folder in 
                    (SELECT "id_folder"
                        FROM "user_folders"
                        WHERE id_user = ?)
        """, (id_user,))
        return cur.fetchall()

    def get_book(self, id_folder):
        cur = self._con.cursor()
        cur.execute("""
            SELECT "mp3", "id_author", "title"
                FROM "folders_mp3"
                WHERE "id_folder" = ?
            """, (id_folder,))
        return cur.fetchall()

    def get_authors(self):
        cur = self._con.cursor()
        cur.execute("""
        SELECT "id_author", "surname", "name", "nick"
            FROM "authors"
        """)
        return cur.fetchall()

    def add_author(self, surname: str, name: str, nick: str):
        try:
            cur = self._con.cursor()
            cur.execute("""
            INSERT INTO "authors" ("surname", "name", "nick")
                VALUES (?, ?, ?);
            """, (surname.strip(), name.strip(), nick.strip()))
            self._con.commit()
        except Exception as e:
            warning(message="Такий автор уже існує")

    def remove_book_user(self, id_user, id_folder):
        cur = self._con.cursor()
        cur.execute("""
        DELETE FROM "user_folders"
            WHERE "id_user" = ? AND "id_folder" = ?
        """, (id_user, id_folder))
        self._con.commit()

    def save_folder_mp3_info(self, path: str, title: str = None, author_id: int = None):
        cur = self._con.cursor()

        if author_id is not None:
            cur.execute("""
            UPDATE "folders_mp3"
                SET "id_author" = ?
                WHERE "mp3" = ?
            """, (author_id, path.strip()))

        if title is not None:
            cur.execute("""
            UPDATE "folders_mp3"
                SET "title" = ?
                WHERE "mp3" = ?
            """, (title.strip(), path.strip()))

        self._con.commit()

    def get_user_book_info(self, id_user: int):
        cur = self._con.cursor()
        cur.execute("""
        SELECT "title", "surname", "name", "nick"
            FROM "user_folders"
            JOIN "folders_mp3"
                ON "folders_mp3"."id_folder" = "user_folders"."id_folder"
            JOIN "authors"
                ON "authors"."id_author" = "folders_mp3"."id_author"
                WHERE "title" is NOT NULL AND "id_user" = ?
        """, (id_user,))
        return cur.fetchall()

    def close(self) -> None:
        self._con.close()
