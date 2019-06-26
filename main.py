#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
from frame.log.log import log
from frame.common.param import *
from frame.thread import ThreadPool
from frame.spider_factory import SpiderFactory

from url.xingzuo_piaoliang import xingzuo_piaoliang2 as xz_pl2
from url.xingzuo_piaoliang import xingzuo_piaoliang3 as xz_pl3
from url.xingzuo_piaoliang import xingzuo_piaoliang4 as xz_pl4

from url.net_d1xz import net_d1xz5 as d1xz5
from url.net_d1xz import net_d1xz5 as d1xz6
from url.net_d1xz import net_d1xz5 as d1xz7
from url.net_d1xz import net_d1xz5 as d1xz8
from url.net_d1xz import net_d1xz5 as d1xz9
from url.net_d1xz import net_d1xz5 as d1xz10
from url.net_d1xz import net_d1xz5 as d1xz11
from url.net_d1xz import net_d1xz5 as d1xz12
from url.net_d1xz import net_d1xz5 as d1xz13
from url.net_d1xz import net_d1xz5 as d1xz14
from url.net_d1xz import net_d1xz5 as d1xz15

if __name__ == '__main__':
    log.info('抓取任务开始执行...')
    spiderFactory = SpiderFactory()
    tpool = ThreadPool()

    """ http://xingzuo.piaoliang.com 开始 """
    # xz2 = spiderFactory.get_spider(COM_PIAOLIANG_NAME)
    # xz2.set_seed_urls(xz_pl2)
    # xz2.set_type(2)
    # xz2.set_seed_urls(xz_pl3)
    # xz2.set_type(3)
    # xz2.set_seed_urls(xz_pl4)
    # xz2.set_type(4)
    # tpool.set_spider(xz2)
    """ http://xingzuo.piaoliang.com 结束 """

    """ https://www.d1xz.net 开始 """
    d1xz = spiderFactory.get_spider(NET_D1XZ_NAME)
    # d1xz.set_seed_urls(d1xz5)
    # d1xz.set_type(5)
    d1xz.set_seed_urls(d1xz6)
    d1xz.set_type(6)
    # d1xz.set_seed_urls(d1xz7)
    # d1xz.set_type(7)
    # d1xz.set_seed_urls(d1xz8)
    # d1xz.set_type(8)
    # d1xz.set_seed_urls(d1xz9)
    # d1xz.set_type(9)
    # d1xz.set_seed_urls(d1xz10)
    # d1xz.set_type(10)
    # d1xz.set_seed_urls(d1xz11)
    # d1xz.set_type(11)
    # d1xz.set_seed_urls(d1xz12)
    # d1xz.set_type(12)
    # d1xz.set_seed_urls(d1xz13)
    # d1xz.set_type(13)
    # d1xz.set_seed_urls(d1xz14)
    # d1xz.set_type(14)
    # d1xz.set_seed_urls(d1xz15)
    # d1xz.set_type(15)
    tpool.set_spider(d1xz)
    """ https://www.d1xz.net 结束 """

    tpool.run()
    log.info('抓取任务完成!')
    exit(0)
