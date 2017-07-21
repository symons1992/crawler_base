#-*- coding:utf-8 -*-

import random
import os


class ProxyClient(object):
    filename = './proxy_data'
    
    def __init__(self):
        file_dir = os.path.split(os.path.realpath(__file__))[0]
        proxy_data_file = os.path.join(file_dir, self.filename)
        self._proxy_list = map(lambda x: x.strip(), 
                open(proxy_data_file).read().split())
        self._proxy_nums = len(self._proxy_list)

    def get_proxy(self):
        proxy = self._proxy_list[random.randint(0, self._proxy_nums-1)]
        print 'got proxy %s' % proxy
        return proxy

