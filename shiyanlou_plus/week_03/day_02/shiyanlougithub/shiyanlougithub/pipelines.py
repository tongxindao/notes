# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from datetime import datetime

from sqlalchemy.orm import sessionmaker

from shiyanlougithub.models import Repository, engine


class ShiyanlougithubPipeline(object):

    def process_item(self, item, spider):
        update_time = re.sub(r'[a-zA-Z]', " ", item["update_time"])
        item["update_time"] = datetime.strptime(update_time, "%Y-%m-%d %H:%M:%S")
        self.session.add(Repository(**item))

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
