# _*_ coding: utf-8 _*_
import requests

class RandomProxy(object):

    def process_request(self, request, spider):
        item = requests.get("http://0.0.0.0:5019/get/").content
        request.meta['proxy'] = "http://{}".format(str(item, encoding="utf-8"))
