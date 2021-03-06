#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
import re
import pyquery
from frame.log.log import log
from frame.common.param import *
from frame.common.get import Get
from frame.common.util import Util
from frame.base.parser import Parser


class COMXzwParser(Parser):
    __doc__ = """ https://www.xzw.com 解析器 """

    def __init__ (self):
        super().__init__()
        _webURL = COM_XZW_WEB_URL
        _parserName = COM_XZW_NAME
        log.info('name:' + self._parserName + ' url:' + self._webURL + ' 解析器安装成功!')

    """ 标题 """

    def _parser_passage_title (self, doc: str) -> (bool, str):
        flag = False
        name = pyquery.PyQuery(doc).find('h3>a').text()
        if None is not name:
            flag = True
        else:
            name = ''
        return flag, name.strip()

    """ 书籍URL """

    def _parser_passage_url (self, doc: str) -> (bool, str):
        flag = False
        url = pyquery.PyQuery(doc).find('h3>a').attr('href')
        if None is not url:
            flag = True
        else:
            url = ''
        url = url.strip()
        url = Util.check_url(url, COM_XZW_WEB_URL)
        return flag, url.strip()

    """ 作者名 """

    def _parser_passage_author (self, doc: str) -> (bool, str):
        flag = False
        author = pyquery.PyQuery(doc).find('body>.wrapper>.main-wraper>.pleft>.viewbox>.sbody>.info>span').text()
        if None is not author:
            author = re.sub(r'(星座|编辑|www.xzw.com|:|：)', '', author)
        else:
            author = ''
        return flag, author.strip()

    """ 内容 + 图片链接 """

    def _parser_passage_content (self, doc: str) -> (bool, str, str, str):
        iindex = 1
        qianyan = ''
        content = ''
        img = {}

        its = pyquery.PyQuery(doc).find('body>.wrapper>.main-wraper>.pleft>.viewbox>.sbody')
        # 获取图片链接
        urls = its.find('img')
        for imgt in urls.items():
            if (None is not imgt) and (None is not imgt.attr('src')):
                img[iindex] = imgt.attr('src')
                iindex += 1
        # 获取图片前内容
        qianyant = its.find('.desc').text()
        if (None is not qianyant) and ('' != qianyant):
            qianyan = qianyant
        # 获取图片后的内容
        for ind in its.find('p').items():
            mc = ind.text()
            if (None is mc) or ('' == mc):
                continue
            mc = re.sub(r'(\n|\r| )', '', mc)
            content += mc + '\n'
        imgUrl = ''
        if len(img) > 0:
            imgUrl = img[1]
        content = re.sub(r'^撰文(:|：)\S+\n', '', content)
        return True, qianyan, imgUrl, content
