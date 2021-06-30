# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy import Item
from pymongo import MongoClient


class OzonPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.ozon

    def process_item(self, item: Item, spider):
        collection = self.mongobase[item['collection']]
        collection.insert_one(item)
        return item
