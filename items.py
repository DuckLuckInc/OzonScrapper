# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OzonItem(scrapy.Item):
    _id = scrapy.Field()
    description = scrapy.Field()
    brand = scrapy.Field()
    characteristics = scrapy.Field()
    images = scrapy.Field()
    price = scrapy.Field()
    categories = scrapy.Field()
    collection = scrapy.Field()
