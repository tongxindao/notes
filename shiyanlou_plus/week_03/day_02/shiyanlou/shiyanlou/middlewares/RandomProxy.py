# _*_ coding: utf-8 _*_
import random


class RandomProxy(object):

    def __init__(self, proxy_ips):
        self.proxy_ips = proxy_ips

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist("PROXY_IPS"))

    def process_request(self, request, spider):
        request.meta['proxy'] = "http://{}".format(random.choice(self.proxy_ips))
