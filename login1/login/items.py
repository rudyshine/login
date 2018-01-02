# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field

class LoginItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    second_url = Field()  #
    title = Field()  #
    final_url = Field()
    head=Field()
    content=Field()
    second_finalurl=Field()
    pass
