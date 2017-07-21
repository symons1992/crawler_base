#-*- coding:utf-8 -*-

from src.cralwer import Crawler


a = Crawler()

cnt = 0
while cnt < 20:
    try:
        a.crawl("http://ip.catr.cn/", need_proxy=True, timeout=10)
        print a.get_raw_data()
        break
    except Exception, e:
        print Exception, e

    cnt += 1

