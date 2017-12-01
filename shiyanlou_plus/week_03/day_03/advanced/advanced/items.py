# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AdvancedItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CourseImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()


class MultipageCourseItem(scrapy.Item):
    name = scrapy.Field()
    image = scrapy.Field()
    author = scrapy.Field()
