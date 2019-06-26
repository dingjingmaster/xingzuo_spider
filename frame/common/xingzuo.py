#!/usr/bin/env python
# -*- encoding=utf8 -*-
import base64
import hashlib
import time

from frame.common.mysql import Mysql
from frame.common.param import *
from frame.log.log import log


class XingZuo:
    def __init__ (self, parser_name: str):
        self._parser_name = parser_name
        self._info = XingZuo.XingZuoInfo()
        self._mysql = XingZuo.XingZuoMysql()

    def get_id (self):
        return self._info.get_id()

    def set_title (self, name):
        self._info.set_title(name)
        return self

    def get_title (self):
        return self._info.get_title()

    def set_author (self, author):
        self._info.set_author(author)
        return self

    def get_author (self):
        return self._info.get_author()

    def set_pageviews (self, num):
        self._info.set_pageviews(num)
        return self

    def get_pageviews (self):
        return self._info.get_pageviews()

    def set_time (self, tim):
        self._info.set_time(tim)
        return self

    def get_time (self):
        return self._info.get_time()

    def set_textTop (self, textTop):
        self._info.set_textTop(textTop)
        return self

    def get_textTop (self):
        return self._info.get_textTop()

    def set_textBottom (self, text):
        self._info.set_textBottom(text)
        return self

    def get_textBottom (self):
        return self._info.get_textBottom()

    def set_type (self, type):
        self._info.set_type(type)
        return self

    def get_type (self):
        return self._info.get_type()

    def set_url (self, url):
        self._info.set_url(url)
        return self

    def get_url (self):
        return self._info.get_url()

    def set_img (self, img):
        self._info.set_img(img)
        return self

    def get_img (self):
        return self._info.get_img()

    """ 文章是否存在 """

    def exist (self, url):
        return self._mysql.passage_info_exist(url)

    """ 保存信息 """

    def save_passage_info (self) -> bool:
        # 检测信息是否存在
        if self._mysql.passage_info_exist(self.get_url()):  # 存在则跳过
            log.info(self.get_title() + '|' + self.get_author() + ' 文章已存在！')
        else:  # 不存在，则插入
            flag, id = self._mysql.insert_passage_info(self.get_title(), self.get_author(), self.get_pageviews(),
                                                       self.get_time(), self.get_textTop(), self.get_img(),
                                                       self.get_textBottom(),
                                                       self.get_type(), self.get_url())
            if not flag:
                return False
            log.info(str(id) + '|' + self.get_title() + '|' + self.get_author() + ' 书籍信息插入成功！')
        return True

    class XingZuoInfo:
        def __init__ (self):
            self._id = -1
            self._title = ''
            self._author = ''
            self._pageviews = 0
            self._time = 0
            self._textTop = ''
            self._img = ''
            self._textBottom = ''
            self._type = 0
            self._url = ''

        def get_id (self):
            return self._id

        def set_title (self, name):
            if None is not name:
                self._title = XingZuo.norm_name(name)
            return self

        def get_title (self):
            return self._title

        def set_author (self, author):
            if None is not author and '' != author:
                self._author = XingZuo.norm_author(author)
            return self

        def get_author (self):
            return self._author

        def set_pageviews (self, num):
            num_int = 0
            try:
                num_int = int(num)
            except:
                pass
            self._pageviews = num_int

        def get_pageviews (self):
            return self._pageviews

        def set_time (self, tim: str):
            tm = 0
            if None != time:
                try:
                    tm = int(tim)
                except:
                    pass
                self._time = tm

        def get_time (self):
            return self._time

        def set_textTop (self, textTop):
            if None != textTop:
                self._textTop = XingZuo.norm_content(textTop)

        def get_textTop (self):
            return self._textTop

        def set_textBottom (self, text):
            if None is not text:
                self._textBottom = XingZuo.norm_content(text)

        def get_textBottom (self):
            return self._textBottom

        def set_type (self, type):
            if None != type:
                self._type = type

        def get_type (self):
            return self._type

        def set_url (self, url):
            if None != url:
                self._url = url

        def get_url (self):
            return self._url

        def set_img (self, img):
            if None != img:
                self._img = img

        def get_img (self):
            return self._img

    # class XingZuoImg:
    #     def __init__(self):
    #         self._id = 0
    #         self._xid = 0
    #         self._img_url = ''
    #         self._img_content = ''
    #         self._name = ''
    #         self._ext_name = ''
    # 
    #     def set_xid(self, cid):
    #         if 0 <= cid:
    #             self._xid = xid
    #         return self
    #     def get_xid(self):
    #         return self._xid
    # 
    #     def get_id(self, nid):
    #         return self._id
    # 
    #     def set_img_url(self, url):
    #         if None != url and '' != url:
    #             self._img_url = url
    # 
    #     def get_img_url(self):
    #         return self._img_url
    # 
    #     def set_img_content(self, content):
    #         if None != content:
    #             self._img_content = content
    #         return self
    #     def get_img_content(self):
    #         return self._img_content
    # 
    #     def set_name(self, name):
    #         if None != name:
    #             self._name = name
    #         return self
    #     def get_name(self):
    #         return self._name
    # 
    #     def set_ext_name(self, ext_name):
    #         if None != ext_name:
    #             self._ext_name = ext_name
    #         return self
    #     def get_ext_name(self):
    #         return self._ext_name

    class XingZuoMysql(Mysql):
        def __init__ (self):
            self.set_database(MYSQL_XingZuo_DB) \
                .set_ip(MYSQL_HOST) \
                .set_port(MYSQL_PORT) \
                .set_usr(MYSQL_USER) \
                .set_password(MYSQL_PASSWORD) \
                .connect()

    @staticmethod
    def norm_name (name: str) -> str:
        # 去掉所有非法字符
        # name = re.sub(r'[\\/:*?"<>|.]', '', name)
        # if None is name:
        #     name = ''
        return name

    @staticmethod
    def norm_author (author: str) -> str:
        # author = re.sub(r'[\\/:*?"<>|.]', '', author)
        # if author is None:
        #     author = ''
        return author

    @staticmethod
    def norm_content (content: str) -> str:
        # content = re.sub(r'[\(（]第一星座网原创文章，转载请联系网站管理人员，否则视为侵权。[\)\）]', '', content)
        return content

    @staticmethod
    def norm_tag (tag: str) -> str:
        # tag = re.sub(r'[\\/:*?"<>|.\[\]]', '', tag)
        # if tag is None:
        #     tag = ''
        return tag

    @staticmethod
    def encode (name: str) -> str:
        if None is name or '' == name:
            return ''
        m2 = hashlib.md5()
        m2.update(base64.b64encode(name.encode('utf8')))
        return m2.hexdigest()
