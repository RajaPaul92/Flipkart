# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HandsanitizerItem(scrapy.Item):
    # define the fields for your item here like:
    sanitizer_name = scrapy.Field()
    sanitizer_rating = scrapy.Field()
    sanitizer_price = scrapy.Field()


