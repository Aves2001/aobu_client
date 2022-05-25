# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter

from ConnectDatabase import ConnectDatabase, params_default


class ParseSitePipeline(object):
    def __init__(self):
        self.con = None

    @classmethod
    def from_crawler(cls, crawler):
        db = cls()
        db.con = ConnectDatabase(*params_default)
        return db

    def process_item(self, item, spider):
        self.con.add_book(item=item)
        return item

    def close_spider(self, spider):
        self.con.close()
