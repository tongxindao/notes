# _*_ coding: utf-8 _*_
import random
from shiyanlou import settings

class RandomProxy(object):

    def process_request(self, request, spider):
        proxy = random.choice(settings.HTTP_PROXY)
        request.meta['proxy'] = proxy
