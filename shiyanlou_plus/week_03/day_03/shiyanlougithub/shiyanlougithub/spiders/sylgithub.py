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
            item = ShiyanlougithubItem()

            item["name"] = course.xpath(".//div[contains(@class, 'd-inline-block')]/h3/a/text()").re_first("([a-zA-Z0-9-_]+)")
            item["update_time"] = course.xpath(".//div[contains(@class, 'text-gray')]/relative-time/@datetime").re_first("(\d{4}-\d{2}-\d{2}\S\d{2}:\d{2}:\d{2})")
            
            course_url = response.urljoin(course.xpath(".//div/h3/a/@href").extract_first())
            request = scrapy.Request(course_url, callback=self.parse_course)
            request.meta["item"] = item

            yield request


    def parse_course(self, response):
        item = response.meta["item"]

        item["commits"] = response.xpath("(//*[@id='js-repo-pjax-container']/div[2]/div[1]/div[3]/div/div/ul/li[1]/a/span)/text()").re_first("[0-9,]+")
        item["branches"] = response.xpath("(//*[@id='js-repo-pjax-container']/div[2]/div[1]/div[3]/div/div/ul/li[2]/a/span)/text()").re_first("[0-9,]+")
        item["releases"] = response.xpath("(//*[@id='js-repo-pjax-container']/div[2]/div[1]/div[3]/div/div/ul/li[3]/a/span)/text()").re_first("[0-9,]+")

        yield item
