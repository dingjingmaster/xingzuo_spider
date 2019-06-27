#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
from frame.common.param import *
from frame.spiders.com_xzw import COMXzwSpider
from frame.spiders.net_d1xz import NTD1zxSpider
from frame.spiders.com_piaoliang import CMPiaoliangSpider


class SpiderFactory:
    def get_spider (self, spider_name: str):
        if spider_name in self._spiderDict:
            return self._spiderDict[spider_name]

    _spiderDict = {
        COM_XZW_NAME:       COMXzwSpider(),
        NET_D1XZ_NAME:      NTD1zxSpider(),
        COM_PIAOLIANG_NAME: CMPiaoliangSpider(),
    }
