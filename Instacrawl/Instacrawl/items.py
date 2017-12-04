# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class InstacrawlItem(scrapy.Item):
    full_name = scrapy.Field()
    username = scrapy.Field()
    bio = scrapy.Field()
    followers = scrapy.Field()
    following = scrapy.Field()
    item_type = scrapy.Field()
