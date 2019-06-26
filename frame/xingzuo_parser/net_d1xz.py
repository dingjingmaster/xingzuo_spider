#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
from frame.base.parser import Parser
from frame.common.param import *
from frame.log.log import log


class NTD1zxParser(Parser):
    __doc__ = """ https://www.d1xz.net 解析器 """

    def __init__ (self):
        super().__init__()
        _webURL = COM_PIAOLIANG_WEB_URL
        _parserName = COM_PIAOLIANG_NAME
        log.info('name:' + self._parserName + ' url:' + self._webURL + ' 解析器安装成功!')
