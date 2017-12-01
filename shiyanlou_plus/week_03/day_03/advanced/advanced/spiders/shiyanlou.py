# -*- coding: utf-8 -*-
import scrapy


class ShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlou'
    # allowed_domains = ['www.shiyanlou.com']
    
    start_urls = ["https://www.shiyanlou.com/courses/63"]

    def parse(self, response):
        yield {
            "name": response.xpath("//h4[contains(@class, 'course-infobox-title')]/span/text()").extract_first(),
            "author": response.xpath("//div[contains(@class, 'mooc-info')]/div/strong/text()").extract_first()
        }

        for url in response.xpath("//div[contains(@class, 'course-content')]/a/@href"):
            yield response.follow(url, callback=self.parse)
