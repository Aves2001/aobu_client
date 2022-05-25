# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaseItem(scrapy.Item):
    # посилання на книжку
    link = scrapy.Field()
    # посилання на фото книжки
    img_link = scrapy.Field()
    # назва книги (яка вказана на сайті)
    title = scrapy.Field()
    # автори книжки
    authors = scrapy.Field()
    # рік випуску книжки
    year = scrapy.Field()
    # жанри в які входить книжка (для поточного сайту)
    genres = scrapy.Field()
    # рейтинг книжки
    rating = scrapy.Field()
    # назва киклу (якщо книга входить в нього)
    cycle_name = scrapy.Field()
    # під яким номером книга в цьому циклі
    cycle_number = scrapy.Field()
    # опис книжки
    brief_content = scrapy.Field()
    # чи книжка в аудіо форматі
    is_audio = scrapy.Field()

class AudioBookItem(BaseItem):
    # читаці книжки
    readers = scrapy.Field()
    # довжина (тривалість) аудіокнижки
    duration = scrapy.Field()


class BazaKnigItem(AudioBookItem):
    pass
