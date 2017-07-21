#-*- coding:utf-8 -*-

import urllib2
from proxy_client import ProxyClient


class Crawler(object):

    def __init__(self):
        self.got_data = ''
        self.proxy_client = ProxyClient()
        pass

    def crawl(self, url, need_proxy=False, timeout=2):
        if need_proxy:
            proxy_handler = urllib2.ProxyHandler(
                {"http": self.proxy_client.get_proxy()})
        else:
            proxy_handler = urllib2.ProxyHandler({})

        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        self.got_data = urllib2.urlopen(url, timeout=timeout).read()

    def get_raw_data(self):
        return self.got_data

    def get_struct_data(self):
        return None

