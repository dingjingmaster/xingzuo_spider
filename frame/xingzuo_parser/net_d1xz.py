#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
import re

import pyquery

from frame.base.parser import Parser
from frame.common.param import *
from frame.common.util import Util
from frame.log.log import log


class NTD1zxParser(Parser):
    __doc__ = """ https://www.d1xz.net 解析器 """

    def __init__ (self):
        super().__init__()
        _webURL = NET_D1XZ_WEB_URL
        _parserName = NET_D1XZ_NAME
        log.info('name:' + self._parserName + ' url:' + self._webURL + ' 解析器安装成功!')

    """ 标题 """

    def _parser_passage_title (self, doc: str) -> (bool, str):
        flag = False
        name = pyquery.PyQuery(doc).find('a').text()
        if None is not name:
            flag = True
        else:
            name = ''
        return flag, name.strip()

    """ 书籍URL """

    def _parser_passage_url (self, doc: str) -> (bool, str):
        flag = False
        url = pyquery.PyQuery(doc).find('a').attr('href')
        if None is not url:
            flag = True
        else:
            url = ''
        url = url.strip()
        url = Util.check_url(url, NET_D1XZ_WEB_URL)
        return flag, url.strip()

    """ 时间 """

    def _parser_passage_date (self, doc: str) -> (bool, str):
        flag = False
        tm = pyquery.PyQuery(doc).find('body>.main>.main_left>.art_con_left>.source>p>span').eq(0).text()
        if None is not tm:
            arr = tm.strip()
        else:
            tm = '1970-12-01 00:00:00'
        return flag, Util.time_str_stamp(tm.strip(), "%Y-%m-%d %H:%M:%S")

    """ 作者名 """

    def _parser_passage_author (self, doc: str) -> (bool, str):
        flag = False
        author = pyquery.PyQuery(doc).find('body>.main>.main_left>.art_con_left>.source>p>span').eq(1).text()
        if None is not author:
            author = re.sub(r'(作者|:|：)', '', author)
        else:
            author = ''
        return flag, author.strip()

    """ 内容 + 图片链接 """

    def _parser_passage_content (self, doc: str) -> (bool, str, str, str):
        iindex = 1
        pindex = 1
        qianyan = ''
        content = ''
        img = {}

        its = pyquery.PyQuery(doc).find('body>.main>.main_left>.art_con_left>.common_det_con')
        # 获取图片链接
        urls = its.find('img')
        for imgt in urls.items():
            if (None is not imgt) and (None is not imgt.attr('src')):
                img[iindex] = imgt.attr('src')
                iindex += 1
        # 获取图片前内容
        qianyant = its.find('p').eq(0).text()
        if (None is not qianyant) and ('' != qianyant):
            qianyan = qianyant
        # 获取图片后的内容
        index = 0
        for ind in its.children().items():
            index += 1
            if index <= 2:
                continue
            mc = ind.text()
            if (None is mc) or ('' == mc):
                continue
            content += mc + '\n'
        imgUrl = ''
        if len(img) > 0:
            imgUrl = img[1]
        return True, qianyan, imgUrl, content
