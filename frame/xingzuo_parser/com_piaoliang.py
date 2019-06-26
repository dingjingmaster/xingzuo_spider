#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
import re

import pyquery

from frame.base.parser import Parser
from frame.common.get import Get
from frame.common.param import *
from frame.common.util import Util
from frame.log.log import log


class CMPiaoliangParser(Parser):
    __doc__ = """ http://xingzuo.piaoliang.com 解析器 """

    def __init__ (self):
        super().__init__()
        _webURL = COM_PIAOLIANG_WEB_URL
        _parserName = COM_PIAOLIANG_NAME
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

    """ 阅读量 """

    def _parser_passage_read (self, doc: str) -> (bool, str):
        flag = False
        num = '0'
        readnum = pyquery.PyQuery(doc).find('.reads').text()
        if None is not readnum:
            flag = True
            num = re.sub(r'(阅读|\(|\)|（|）)', '', readnum)
        if '' == num:
            num = '0'
        return flag, num.strip()

    """ 书籍URL """

    def _parser_passage_url (self, doc: str) -> (bool, str):
        flag = False
        url = pyquery.PyQuery(doc).find('h3>a').attr('href')
        if None is not url:
            flag = True
        else:
            url = ''
        return flag, url.strip()

    """ 时间 """

    def _parser_passage_date (self, doc: str) -> (bool, str):
        flag = False
        tm = pyquery.PyQuery(doc).find('body>.main-wrap>.m-wrap>.main-part>.sbody>.info>.s1').text()
        if None is not tm:
            tm = re.sub(r'(时间|:|：)', '', tm)
            arr = tm.strip().split(' ')
            tm = arr[0]
        else:
            tm = '1970-12-01'
        return flag, Util.time_str_stamp(tm.strip(), "%Y-%m-%d")

    """ 作者名 """

    def _parser_passage_author (self, doc: str) -> (bool, str):
        flag = False
        author = pyquery.PyQuery(doc).find('body>.main-wrap>.m-wrap>.main-part>.sbody>.info>.s1>small').text()
        if None is not author:
            author = re.sub(r'(来源|:|：)', '', author)
        else:
            author = ''
        return flag, author.strip()

    """ 内容 + 图片链接 """

    def _parser_passage_content (self, doc: str) -> (bool, str, str, str):
        flag = False
        iindex = 1
        pindex = 1
        qianyan = ''
        content = ''
        img = {}
        fanye = ''
        hasNextPage = False
        loop = True

        mdoc = doc

        while loop:
            imgstr = ''
            hasNextPage = False
            its = pyquery.PyQuery(mdoc).find('body>.main-wrap>.m-wrap>.main-part>.sbody>.view_content')
            # 获取图片链接
            urls = its.find('img')
            for imgt in urls.items():
                if (None is not imgt) and (None is not imgt.attr('src')):
                    img[iindex] = imgt.attr('src')
                    iindex += 1
            # 获取前言
            qianyant = its.find('.content_digest').text()
            if (None is not qianyant) and ('' != qianyant):
                qianyan = qianyant

            # 检查是否有翻页
            fanye = ''
            pagetion = pyquery.PyQuery(mdoc).find('body>.main-wrap>.m-wrap>.main-part>.pagetion>a')
            for it in pagetion.items():
                page = it.text()
                url = it.attr('href')
                if (None is page) or ('' == page) or (None is url):
                    continue
                if int(page) >= pindex:
                    hasNextPage = True
                    fanye = url
            if '' != fanye:
                ttext = Get(fanye).html()
                if '' != ttext:
                    mdoc = ttext
            if '' == fanye:
                loop = False
                flag = True
            # 获取内容
            ctt = ''
            if (1 == pindex) and (hasNextPage == True):
                ctt = its.find('p').eq(1).text()
            else:
                ctt = its.find('div').eq(3).text()
            if '' == ctt:
                ctt = its.text()
            if None is not ctt:
                content += ctt + '\n'
            pindex += 1
        imgUrl = ''
        if len(img) > 0:
            imgUrl = img[1]
        return flag, qianyan, imgUrl, content
