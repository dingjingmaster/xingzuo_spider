#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
from frame.log.log import log
from frame.common.param import *
from frame.thread import ThreadPool
from frame.spider_factory import SpiderFactory

from url.xingzuo_piaoliang import xingzuo_piaoliang2 as xz_pl2
from url.xingzuo_piaoliang import xingzuo_piaoliang3 as xz_pl3
from url.xingzuo_piaoliang import xingzuo_piaoliang4 as xz_pl4


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
    """ https://www.d1xz.net 结束 """

    tpool.run()
    log.info('抓取任务完成!')
    exit(0)
