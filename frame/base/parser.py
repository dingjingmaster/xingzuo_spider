#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
import pyquery

"""
    需求字段：
        标题、发表日期、浏览量、内容来源或作者、内容、图片url、
        类型（1：星座综合类、2：星座排行类、3：星座职场类、4：星座时尚类、5：星座个性类、
            6：星座知识类、7：星座爱情类、8：测试爱情类、9：测试性格类、10：测试趣味类、
            11：测试财富类、12：测试智商类、13：测试职业类、14：测试社交类、15：测试综合类、
            16：生肖综合类）
    
    需要的字段信息
        1. 网站根URL
        2. 解析器名字
        3. 解析器类型
            1. PARSER_PASSAGE_URL               文章URL
            2. PARSER_PASSAGE_TITLE             文章标题
            3. PARSER_PASSAGE_AUTHOR            文章作者/来源
            3. PARSER_PASSAGE_READ              阅读量
            4. PARSER_PASSAGE_DATE              发表日期
            5. PARSER_PASSAGE_CONTENT           文章内容
            6. PARSER_PASSAGE_IMGURL            文章中的图片 URL
            7. PARSER_PASSAGE_TYPE              文章类型
"""


class Parser(object):
    def __init__ (self):
        self._webURL = ''
        self._parserName = 'base_parser'

    def _parser_passage_url (self, doc: str) -> (bool, str):
        return

    def _parser_passage_title (self, doc: str) -> (bool, str):
        return

    def _parser_passage_author (self, doc: str) -> (bool, str):
        return

    def _parser_passage_read (self, doc: str) -> (bool, str):
        return

    def _parser_passage_date (self, doc: str) -> (bool, str):
        return

    def _parser_passage_content (self, doc: str) -> (bool, str, str, str):
        return

    def _parser_passage_img_url (self, doc: str) -> (bool, str):
        return

    def _parser_passage_type (self, doc: str) -> (bool, str):
        return

    def get_parser_name (self):
        return self._parserName

    @staticmethod
    def _parser (doc: str, rule: str):
        return pyquery.PyQuery(doc).find(rule)

    def parse (self, doc: str, rule='', parse_type=-1):
        if self.PARSER_PASSAGE_URL == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_url(doc)
        elif self.PARSER_PASSAGE_TITLE == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_title(doc)
        elif self.PARSER_PASSAGE_AUTHOR == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_author(doc)
        elif self.PARSER_PASSAGE_READ == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_read(doc)
        elif self.PARSER_PASSAGE_DATE == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_date(doc)
        elif self.PARSER_PASSAGE_CONTENT == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_content(doc)
        elif self.PARSER_PASSAGE_IMGURL == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_img_url(doc)
        elif self.PARSER_PASSAGE_TYPE == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_type(doc)
        else:
            if doc == '' or doc == None:
                return (False, '')
            return Parser._parser(doc, rule)

    PARSER_PASSAGE_URL = 1
    PARSER_PASSAGE_TITLE = 2
    PARSER_PASSAGE_AUTHOR = 3
    PARSER_PASSAGE_READ = 4
    PARSER_PASSAGE_DATE = 5
    PARSER_PASSAGE_CONTENT = 6
    PARSER_PASSAGE_IMGURL = 7
    PARSER_PASSAGE_TYPE = 8
