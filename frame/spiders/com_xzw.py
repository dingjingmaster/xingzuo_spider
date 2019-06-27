#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-

from frame.base.spider import Spider
from frame.common.param import *
from frame.common.xingzuo import XingZuo
from frame.log.log import log
from frame.parser_factory import get_parser


class COMXzwSpider(Spider):
    def __init__ (self):
        super().__init__()
        self._name = COM_XZW_NAME
        self._webURL = COM_XZW_WEB_URL
        log.info('name:' + self._name + ' url:' + self._webURL + ' spider安装成功!')

    def check (self):
        pass

    def run(self):
        parser = get_parser().get_parser(COM_XZW_NAME)
        for url in self.get_passage_list():
            arr = url.split('|')
            url = arr[0]
            type = int(arr[1])
            text = Spider.http_get(url)
            if '' == text:
                continue
            doc = parser.parse(text, rule='body>.wrapper>#list>.main>.l-item>ul')
            for ct in doc.children().items():
                passage = XingZuo(COM_XZW_NAME)
                flag, name = parser.parse(ct.html(), parse_type=parser.PARSER_PASSAGE_TITLE)
                if flag:
                    passage.set_title(name)
                flag, passage_url = parser.parse(ct.html(), parse_type=parser.PARSER_PASSAGE_URL)
                if not flag:
                    continue
                passage.set_url(passage_url)
                # 检测文章是否存在
                if passage.exist(passage_url):
                    log.info(name + '已存在!')
                    continue
                # 获取文章内容
                text1 = Spider.http_get(passage_url)
                if '' == text1:
                    continue
                flag, author = parser.parse(text1, parse_type=parser.PARSER_PASSAGE_AUTHOR)
                passage.set_author(author)
                # 获取 内容、图片链接
                flag, top, img, bottom = parser.parse(text1, parse_type=parser.PARSER_PASSAGE_CONTENT)
                if flag:
                    passage.set_img(img)
                    passage.set_textTop(top)
                    passage.set_textBottom(bottom)
                    passage.set_type(type)
                    if '' == bottom or '' == top or '' == name or '' == passage_url:
                        continue
                    passage.save_passage_info()
                    log.info(name + '|' + author + ' 抓取成功!')
                else:
                    log.warn(name + '抓取失败！')
        log.info(self._name + '执行完成!')

    def get_passage_list (self):
        if len(self._seedURL) <= 0:
            log.error(self._name + '由于未定义seed url 导致获取book list 失败！')
            return None
        try:
            for ik, iv in self._seedURL.items():
                arr1 = ik.split('|')
                arr2 = iv.split('|')
                arr3 = arr1[1].split('-')
                for x in range(int(arr2[0]), int(arr2[1]) + 1):
                    if x == 1:
                        self._bookList.append(arr1[0][:-2] + '|' + arr3[1])
                        continue
                    self._bookList.append(arr1[0] + str(x) + arr3[0] + '|' + arr3[1])
            for i in self._bookList:
                yield i
        except Exception as e:
            log.error(self._name + '不符合的seed url 设置: ' + str(e))
            return None