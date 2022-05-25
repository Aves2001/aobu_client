def gen_INSERT_sites():
    return """INSERT IGNORE INTO `sites` (`name`, `link`) VALUES (@site_link, @site_link)"""


def gen_SET_id_site():
    return """SET
        @id_site = (
        SELECT
            id_site
        FROM
            sites
        WHERE
            sites.link = @site_link
    )"""


def gen_fill_sql_add_book(item):
    sql = list()
    sql.append(gen_INSERT_book_title())
    books_from_websites = gen_INSERT_books_from_websites().split(';')
    books_from_websites = [f"{i};".strip('\n') for i in books_from_websites if len(i) > 0]
    sql.extend(books_from_websites)

    sql.append(gen_INSERT_authors(item['authors']))
    sql.append(gen_INSERT_books_authors(item['authors']))

    characteristics = gen_INSERT_characteristics().split(';')
    for characteristic in characteristics:
        if len(characteristic) > 2:
            sql.append(f'{characteristic.strip()};')

    sql.append(gen_INSERT_cycle_name())

    try:
        cycle_number = gen_INSERT_cycle(item['cycle_number']).split(';')
        for cn in cycle_number:
            if len(cn) > 5:
                sql.append(f'{cn.strip()};')
    except:
        pass

    sql.append(gen_INSERT_sites())
    sql.append(gen_SET_id_site())

    sites_genres = gen_INSERT_sites_genres(item['genres']).split(';')
    for i in sites_genres:
        if len(i) > 5:
            sql.append(f"{i.strip()};")

    sql.append(gen_INSERT_books_genres(item['genres']))

    sql.append(gen_insert_readers(item['readers']))
    sql.append(gen_INSERT_books_readers(item['readers']))

    for i, item in enumerate(sql):
        sql[i] = ' '.join(item.split())

    return sql


def gen_INSERT_SET(item):
    """Змінні"""
    sql = list()
    value = list()
    for it in item:
        if it == "authors":
            for i, author in enumerate(clear_fio_list(item[it])):
                if len(author) == 2:
                    value.append(author[0])
                    value.append(author[1])
                    sql.append(f"SET @a_surname_{i} = %s;")
                    sql.append(f"SET @a_name_{i} = %s;")
                if len(author) == 1:
                    value.append(author[0])
                    sql.append(f"SET @a_nickname_{i} = %s;")
        if it == "cycle_name":
            sql.append("SET @cycle_name = %s;")
            value.append(item[it])
        if it == "cycle_number":
            try:
                _ = int(item[it])
                value.append(int(item[it]))
                sql.append("SET @number_cycle = %s;")
            except:
                num = item[it].split('-')
                num = int(num[0]), int(num[1])
                for i in range(num[0], num[1] + 1):
                    value.append(i)
                    sql.append(f"SET @number_cycle_{i} = %s;")

        if it == "duration":
            sql.append("SET @duration = %s;")
            value.append(item[it])

        if it == "genres":
            for i, genre in enumerate(item[it]):
                sql.append(f"SET @genre_{i} = %s;")
                value.append(genre)

        if it == "img_link":
            value.append(item[it])
            sql.append("SET @image = %s;")

        if it == "link":
            value.append(item[it])
            site_link = str(item[it]).split('/')[:3]
            site_link = "/".join(site_link)
            value.append(site_link)
            sql.append("SET @link = %s;")
            sql.append("SET @site_link = %s;")

        if it == "rating":
            rating = None
            try:
                rating = item[it]
            except:
                rating = None
            finally:
                value.append(rating)
                sql.append("SET @rating = %s;")

        if it == "readers":
            for i, fio in enumerate(clear_fio_list(item[it])):
                if len(fio) == 2:
                    sql.append(f"SET @r_surname_{i} = %s;")
                    sql.append(f"SET @r_name_{i} = %s;")
                    value.append(fio[0])
                    value.append(fio[1])
                if len(fio) == 1:
                    sql.append(f"SET @r_nickname_{i} = %s;")
                    value.append(fio[0])

        if it == "title":
            sql.append("SET @title = %s;")
            value.append(item[it])

        if it == "year":
            sql.append("SET @year = %s;")
            value.append(int(item[it]))

        if it == "brief_content":
            sql.append("SET @brief_content = %s;")
            value.append(str(item[it]))

        if it == "is_audio":
            value.append(1)
            sql.append("SET @is_audio = %s")

    return sql, value


def gen_INSERT_book_title():
    """додавання заголовка книжки"""
    return f"""
    INSERT IGNORE
    INTO book_title (book_title)
    VALUES(@title);
"""

def gen_INSERT_books_from_websites():
    """інформаця про книжку на поточному сайті"""
    return """
INSERT INTO books_from_websites(
    book_title,
    image,
    brief_content,
    is_audio,
    link,
    info_update_date
)
VALUES(
    (
    SELECT
        book_title.id_book_title
    FROM
        book_title
    WHERE
        book_title.book_title = @title
),
@image,
@brief_content,
@is_audio,
@link,
DEFAULT
);
SET @id_book = ( SELECT LAST_INSERT_ID() );"""


def gen_INSERT_authors(authors: list):
    """додавання автора, до списку авторів"""
    value = ""
    for i, autor in enumerate(clear_fio_list(authors)):
        if len(autor) == 2:
            value = f"{value}(@a_name_{i}, @a_surname_{i}, DEFAULT, DEFAULT),\n"
        if len(autor) == 1:
            value = f"{value}(DEFAULT, DEFAULT, @a_nickname_{i}, DEFAULT),\n"
    value = f"VALUES\n{value[:-2]};"
    return f"""
    INSERT IGNORE
    INTO authors(
        authors.name,
        authors.surname,
        authors.nickname,
        authors.info_update_date
    )
{value}
    """


def clear_fio_list(fio: list):
    for f in fio:
        yield f.split()


def gen_INSERT_books_authors(authors: list):
    """співвідношення автора і кнжки"""
    value = ""
    for i, autor in enumerate(clear_fio_list(authors)):
        if len(autor) == 2:
            value = f"""{value}(@id_book, ( SELECT authors.id_author FROM authors
        WHERE
            authors.name = @a_name_{i} AND authors.surname = @a_surname_{i}
        )),
"""
        if len(autor) == 1:
            value = f"""{value}(@id_book, ( SELECT authors.id_author FROM authors
        WHERE
            authors.nickname = @a_nickname_{i}
        )),
"""

    value = f"VALUES {value[:-2]};"
    return f"""
INSERT INTO books_authors(
    books_authors.id_book,
    books_authors.id_author
)
{value}
"""

def gen_INSERT_characteristics():
    """характеристики книжки"""
    return """
    INSERT INTO books_year
    VALUES (@id_book, @year);

    INSERT INTO `books_duration` (`id_book`, `duration`) 
    VALUES (@id_book, @duration);
    
    INSERT INTO `books_rating`(`id_book`, `rating`)
    VALUES (@id_book, @rating)
"""

def gen_INSERT_cycle_name():
    """додавання назви цикла"""
    return """
    INSERT IGNORE
    INTO cycle_name(cycle_name.name)
    VALUES(@cycle_name);
    """

def gen_INSERT_cycle(number_cycle: str):
    """додавання книжки до цикла"""
    values = ""

    if number_cycle.isnumeric():
        values = f"{values}(@id_book, @cycle_id, @number_cycle),\n"
    else:
        num = number_cycle.split('-')
        num = int(num[0]), int(num[1])
        for i in range(num[0], num[1]+1):
            values = f"{values}(@id_book, @cycle_id, @number_cycle_{i}),\n"
    values = f"VALUES {values[:-2]};"
    return f"""
    SET @cycle_id = ( SELECT cycle_name.id FROM cycle_name
        WHERE
            cycle_name.name = @cycle_name
    );

    INSERT INTO cycle(
        cycle.id_book,
        cycle.cycle_name,
        cycle.number
    )
{values}
"""

def gen_INSERT_sites_genres(genres: list):
    """додавання жанрів до списку жажнів"""
    value = ""
    for i, _ in enumerate(genres):
        value = f"{value} (@id_site, @genre_{i}),\n"
    value = f"VALUES {value[:-2]};"
    return f"""
    INSERT IGNORE
    INTO sites_genres(
        sites_genres.id_site,
        sites_genres.genre
    )
{value}
    """

def gen_INSERT_books_genres(genres: list):
    """cпіввідношення жанрів і книжки"""
    value = ""
    for i, genre in enumerate(genres):
        value = f"""{value}
        (@id_book, ( SELECT sites_genres.id_genre FROM sites_genres
        WHERE
            sites_genres.id_site = @id_site AND sites_genres.genre = @genre_{i})),
"""
    value = f"VALUES{value[0:-2]};"
    return f"""
INSERT INTO books_genres
{value}
"""


def gen_insert_readers(readers: list):
    """додавання читачів"""
    value = ""
    for i, autor in enumerate(clear_fio_list(readers)):
        if len(autor) == 2:
            value = f"{value}(@r_name_{i}, @r_surname_{i}, DEFAULT, DEFAULT),\n"
        if len(autor) == 1:
            value = f"{value}(DEFAULT, DEFAULT, @r_nickname_{i}, DEFAULT),\n"

    value = f"VALUES{value[:-2]};"
    return f"""
    INSERT IGNORE
    INTO readers(
        name,
        surname,
        nickname,
        info_update_date
    )
{value}
"""


def gen_INSERT_books_readers(readers: list):
    """cпіввідношення читачів і книжки"""
    value = ""
    for i, autor in enumerate(clear_fio_list(readers)):
        if len(autor) == 2:
            value = f"""{value}(@id_book,( SELECT readers.id_reader FROM readers
        WHERE
            readers.name = @r_name_{i} AND readers.surname = @r_surname_{i})),
"""
        if len(autor) == 1:
            value = f"""{value}(@id_book,( SELECT readers.id_reader FROM readers
                    WHERE
                        readers.nickname = @r_nickname_{i})),
"""
    value = f"VALUES {value[:-2]};"
    return f"""
    INSERT INTO books_readers
    {value}
"""
