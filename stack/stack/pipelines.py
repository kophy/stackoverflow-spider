# -*- coding: utf-8 -*-

import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings["MONGODB_SERVER"],
            settings["MONGODB_PORT"]
        );
        db = connection[settings["MONGODB_DB"]];
        self.collection = db[settings["MONGODB_COLLECTION"]];

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Missing data!");
        self.collection.update({"url": item["url"]}, dict(item), upsert = True);
        log.msg("Question added to MongoDB database!", level = log.DEBUG, spider = spider);
        return item;
