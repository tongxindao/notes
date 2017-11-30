# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem 


class SylgithubSpider(scrapy.Spider):
    name = 'sylgithub'
    # allowed_domains = ['github.com']
    
    @property
    def start_urls(self):
        url_tmpl = url_tmpl = "https://github.com/shiyanlou?page={}&tab=repositories"
        return (url_tmpl.format(i) for i in range(1, 5))


    def parse(self, response):
        for course in response.xpath("//*[@id='user-repositories-list']/ul/li"):
            item = ShiyanlougithubItem({
                "name": course.xpath(".//div[contains(@class, 'd-inline-block')]/h3/a/text()").re_first("(\w+)"),
                "update_time": course.xpath(".//div[contains(@class, 'text-gray')]/relative-time/@datetime").re_first("(\d{4}-\d{2}-\d{2}\S\d{2}:\d{2}:\d{2})")
            })

            yield item
