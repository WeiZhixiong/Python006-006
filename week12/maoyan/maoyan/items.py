# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoYanItem(scrapy.Item):
    movie_name = scrapy.Field()
    movie_type = scrapy.Field()
    show_time = scrapy.Field()
