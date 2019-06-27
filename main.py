#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
from frame.log.log import log
from frame.common.param import *
from frame.thread import ThreadPool
from url.net_d1xz import net_d1xz as d1xz
from url.com_xzw import com_xzw as com_xzw
from frame.spider_factory import SpiderFactory
from url.xingzuo_piaoliang import xingzuo_piaoliang as xz_pl

if __name__ == '__main__':
    log.info('抓取任务开始执行...')
    spiderFactory = SpiderFactory()
    tpool = ThreadPool()

    """ http://xingzuo.piaoliang.com 开始 """
    # xz = spiderFactory.get_spider(COM_PIAOLIANG_NAME)
    # xz.set_seed_urls(xz_pl)
    # tpool.set_spider(xz)
    """ http://xingzuo.piaoliang.com 结束 """

    """ https://www.d1xz.net 开始 """
    # d1xz = spiderFactory.get_spider(NET_D1XZ_NAME)
    # d1xz.set_seed_urls(d1xz)
    # tpool.set_spider(d1xz)
    """ https://www.d1xz.net 结束 """

    """ https://www.xzw.com 开始 """
    xzw = spiderFactory.get_spider(COM_XZW_NAME)
    xzw.set_seed_urls(com_xzw)
    tpool.set_spider(xzw)
    """ https://www.xzw.com 结束 """

    tpool.run()
    log.info('抓取任务完成!')
    exit(0)
