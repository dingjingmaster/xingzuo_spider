#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-

from frame.base.spider import Spider
from frame.common.param import *
from frame.log.log import log
from frame.parser_factory import get_parser


class NTD1zxSpider(Spider):
    def __init__ (self):
        self._name = COM_PIAOLIANG_NAME
        self._webURL = COM_PIAOLIANG_WEB_URL
        log.info('name:' + self._name + ' url:' + self._webURL + ' spider安装成功!')

    def check (self):
        pass

    def run (self):
        parser = get_parser().get_parser(COM_PIAOLIANG_NAME)
