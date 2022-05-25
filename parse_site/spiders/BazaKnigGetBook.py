import scrapy

from parse_site.items import BazaKnigItem


class BazaKnigGetBook(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.urls = kwargs.get("urls", None)

    name = "BazaKnigGetBook"

    def start_requests(self):
        urls = self.urls

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = BazaKnigItem()

        item['is_audio'] = 1

        item['link'] = response.url
        item['img_link'] = response.css(".full-img img::attr(src)").get()

        title = response.css("title::text").get()
        item['title'] = clear_title(title=title)

        full_items = dict()
        for li in response.css(".full ul.full-items li"):
            full_items.update(
                clear_li_text(
                    li.css("::text").getall()
                )
            )

        item['authors'] = full_items['Автор']
        item['readers'] = full_items['Читает']
        item['year'] = full_items['Год']
        item['duration'] = full_items['Длительность']
        try:
            item['cycle_name'] = full_items['Цикл'][0]
            item['cycle_number'] = full_items['Цикл'][1]
        except:
            pass
        item['genres'] = full_items['Жанр']
        item['rating'] = clear_rating(
            response.css(".main-sliders-rate a::text").getall()
        )

        brief_content = response.css(".full .short-text::text").getall()
        item['brief_content'] = "\n".join([i.strip() for i in brief_content if len(i.strip()) > 0])

        # print(item)
        yield item


def clear_rating(rating: list):
    rating = [i.strip() for i in rating]
    rating = [int(i) for i in rating if i != '' and i.isnumeric()]
    return rating[0] - rating[1]


def clear_title(title: str):
    return " ".join(title.split()[1:-4])


def clear_li_text(line, key_cycle="Цикл", key_year="Год", key_duration="Длительность"):
    key = line[0][0:-2]
    value = line[1:]

    for v_line in value:
        if len(v_line) < 4 and v_line != key_cycle:
            value.remove(v_line)
    if key == key_cycle:
        value[1] = value[1].replace('(', '').replace(')', '')
    if key == key_year or key == key_duration:
        value = value[0]
    return {
        key: value
    }
