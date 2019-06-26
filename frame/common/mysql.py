#!/usr/bin/env python
# -*- encoding=utf8 -*-
import time
import pymysql
import threading
from frame.common.util import Util
from frame.log.log import log


class Mysql(object):
    _mutex = threading.Lock()
    _host = ''
    _db = ''
    _port = 3306
    _user = ''
    _password = ''
    _connect = None

    def set_ip(self, host: str):
        self._host = host
        return self

    def set_port(self, port: int):
        self._port = port
        return self

    def set_database(self, db: str):
        self._db = db
        return self

    def set_usr(self, usr: str):
        self._user = usr
        return self

    def set_password(self, password: str):
        self._password = password
        return self

    def connect(self):
        self._connect = pymysql.Connect(
            host=self._host,
            port=self._port,
            user=self._user,
            db=self._db,
            passwd=self._password,
            charset='utf8'
        )
        return self

    """ 文章 url 是否存在 """
    def passage_info_exist(self, url) -> bool:
        flag = False
        id = -1
        msql = 'SELECT `id` FROM `article` WHERE url = "{url}";'.format(url = url)
        try:
            cursor = self._connect.cursor()
            cursor.execute(msql)
            self._connect.commit()
            result = cursor.fetchone()
            if None is not result:
                flag = True
        except Exception as e:
            log.error('MySQL 执行错误: ' + str(e))
        return flag

    """ 根据文章 url 插入信息 """
    def insert_passage_info(self, title: str, author: str, pageviews: int, tim: int,\
                            textTop: str, img: str, textBottom: str, type: int, url: str):
        flag = False
        id = -1
        # 检查关键字段是否存在
        if (not Util.valid(title)) or (not Util.valid(author)):
            return flag, -1
        msql = 'INSERT INTO `article` (' \
               '`title`, `author`, `pageviews`, `time`, `textTop`, `img`, `textbottom`, `type`, `url`)' \
               ' VALUES ("{title}", "{author}", "{pageviews}", "{tim}", "{textTop}", "{img}", "{textBottom}",' \
               ' "{type}", "{url}");'.format (
            title = self._connect.escape_string(title), author = self._connect.escape_string(author),
            pageviews = pageviews, tim = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tim)),
            textTop = self._connect.escape_string(textTop), img = self._connect.escape_string(img),
            textBottom = self._connect.escape_string(textBottom), type = type,
            url = self._connect.escape_string(url));
        try:
            curosr = self._connect.cursor()
            curosr.execute(msql)
            self._connect.commit()
            id = int(curosr.lastrowid)
            if id >= 0:
                flag = True
                log.info('id=%d, name=%s, author=%s,信息保存成功' % (id, title, author))
            else:
                log.error(title + '|' + author + '信息保存失败!')
        except Exception as e:
            log.error('MySQL 执行错误: ' + str(e))
        return flag, id

    """ 保存文章内容 """

    # """ ok """
    # def insert_novel_info(self, name: str, author: str, category: str, describe: str, complete: int, parser: str,
    #                       book_url: str, img_url: str, img_content: str, chapter_base_url: str,
    #                       create_time: int, update_time: int) -> (bool, int):
    #     flag = False
    #     novel_id = -1
    #     msql = 'INSERT INTO `novel_info` (`name`, `author`, `category`, `describe`, `complete`, `parser`, `book_url`,'\
    #            ' `img_url`, `img_content`, `chapter_base_url`, `create_time`, `update_time`)' \
    #            ' VALUES ("{name}", "{author}", "{category}", "{describe}", "{complete}", "{parser}", "{book_url}",' \
    #            ' "{img_url}", "{img_content}", "{chapter_base_url}", "{create_time}", "{update_time}");'\
    #         .format(name=self._connect.escape_string(name), author=self._connect.escape_string(author),
    #                 category=self._connect.escape_string(category), describe=self._connect.escape_string(describe),
    #                 complete=complete, parser=self._connect.escape_string(parser),
    #                 book_url=self._connect.escape_string(book_url), img_url=self._connect.escape_string(img_url),
    #                 img_content=self._connect.escape_string(str(img_content)),
    #                 chapter_base_url=self._connect.escape_string(chapter_base_url),
    #                 create_time=create_time, update_time=update_time)
    #     try:
    #         curosr = self._connect.cursor()
    #         curosr.execute(msql)
    #         self._connect.commit()
    #         novel_id = int(curosr.lastrowid)
    #         if novel_id >= 0:
    #             flag = True
    #             log.info(name + '|' + author + '信息保存成功!')
    #         else:
    #             log.error(name + '|' + author + '信息保存失败!')
    #     except Exception as e:
    #         log.error('MySQL 执行错误: ' + str(e))
    #     return flag, novel_id
    #
    # """ 根据URL更新书籍信息 """
    # def update_novel_info_by_url(self, book_url: str, name: str, author: str, category: str, describe: str,
    #                              complete: int, img_url: str, img_content: str, chapter_base_url: str, update_time: int):
    #     msql = 'UPDATE `novel_info` SET `name`="{name}", `author`="{author}", `category`="{category}", \
    #             `describe`="{describe}", `complete`="{complete}", `img_url`="{img_url}", `img_content`="{img_content}",\
    #             `chapter_base_url`="{chapter_base_url}", `update_time`="{update_time}" WHERE `book_url`="{book_url}";'\
    #             .format(name=self._connect.escape_string(name), author=self._connect.escape_string(author),
    #                     category=self._connect.escape_string(category), describe=self._connect.escape_string(describe),
    #                     complete=complete, img_url=self._connect.escape_string(img_url),
    #                     img_content=self._connect.escape_string(str(img_content)),
    #                     chapter_base_url=self._connect.escape_string(chapter_base_url),
    #                     update_time=update_time, book_url=self._connect.escape_string(book_url))
    #     try:
    #         curosr = self._connect.cursor()
    #         curosr.execute(msql)
    #         self._connect.commit()
    #         log.info(name + '|' + author + '信息更新成功！')
    #     except Exception as e:
    #         log.error('MySQL 执行错误: ' + str(e))
    #     return None
    #
    # """ 根据URL插入书籍信息 """
    # def insert_novel_chapter(self, novel_id: int, index: int, chapter_url: str, parser: str,
    #                          name: str, content: str, update_time: int):
    #     msql = 'INSERT INTO `novel_chapter` (`nid`, `index`, `chapter_url`,`parser`,\
    #         `name`, `content`, `update_time`) VALUES \
    #          ("{nid}", "{index}", "{chapter_url}", "{parser}", "{name}", "{content}", "{update_time}");' \
    #         .format(nid=novel_id, index=index, chapter_url=self._connect.escape_string(chapter_url),
    #                 parser=self._connect.escape_string(parser), name=self._connect.escape_string(name),
    #                 content=self._connect.escape_string(str(content)), update_time=update_time)
    #     try:
    #         cursor = self._connect.cursor()
    #         cursor.execute(msql)
    #         self._connect.commit()
    #         log.info(str(index) + '|' + name + '|' + chapter_url + ' 章节信息插入成功！')
    #     except Exception as e:
    #         log.error('插入章节' + name + '错误：' + str(e))
    #         return False
    #     return True
    #
    # """ 根据URL更新书籍章节 """
    # def update_novel_chapter_by_url(self, novel_id: int, index: int, chapter_url: str, name: str,
    #                                 content: str, update_time: int) -> bool:
    #     msql = 'UPDATE `novel_chapter` SET `nid` = "{nid}", `index`="{index}", `name`="{name}",\
    #         `content`="{content}", `update_time`="{update_time}" WHERE `chapter_url`="{chapter_url}";'\
    #         .format(nid=novel_id, index=index, name=self._connect.escape_string(name),
    #                 content=self._connect.escape_string(content), update_time=update_time,
    #                 chapter_url=self._connect.escape_string(chapter_url))
    #     try:
    #         curosr = self._connect.cursor()
    #         curosr.execute(msql)
    #         self._connect.commit()
    #         log.info(str(index) + '|' + name + '|' + chapter_url + ' 章节信息更新成功！')
    #     except Exception as e:
    #         log.error('章节信息更新失败: ' + str(e))
    #         return False
    #     return True
    #
    # """ 根据URL更新小说封面图片URL """
    # def update_novel_info_img_url_by_url(self, book_url: str, img_url: str):
    #     if self.novel_info_is_locked_by_url(book_url):
    #         log.info('书籍信息被锁!不可修改!')
    #         return True
    #     if self.novel_info_exist(book_url):  # 小说信息存在，更新
    #         msql = 'UPDATE `novel_info` SET img_url = "{img_url}", `update_time`="{update}"\
    #                 WHERE book_url = "{book_url}";'\
    #                 .format(img_url=self._connect.escape_string(str(img_url)),
    #                         book_url=self._connect.escape_string(book_url),
    #                         update=int(time.time()))
    #         try:
    #             curosr = self._connect.cursor()
    #             curosr.execute(msql)
    #             self._connect.commit()
    #         except Exception as e:
    #             log.error('书籍封面页URL更新失败：: ' + str(e))
    #             return False
    #         else:
    #             log.error('要更新的小说信息不存在！')
    #             return False
    #     return True
    #
    # """ 根据URL更新小说封面图片 """
    # def update_novel_info_img_content_by_url(self, book_url: str, img_content: str):
    #     if self.novel_info_is_locked_by_url(book_url):
    #         log.info('书籍信息被锁!不可修改!')
    #         return True
    #     if self.novel_info_exist(book_url):  # 小说信息存在，更新
    #         msql = 'UPDATE `novel_info` SET img_content = "{img_content}", `update_time`="{update}"\
    #                     WHERE book_url = "{book_url}";' \
    #             .format(img_content=self._connect.escape_string(str(img_content)),
    #                     book_url=self._connect.escape_string(book_url),
    #                     update=int(time.time()))
    #         try:
    #             curosr = self._connect.cursor()
    #             curosr.execute(msql)
    #             self._connect.commit()
    #         except Exception as e:
    #             log.error('书籍封面页更新失败：: ' + str(e))
    #             return False
    #         else:
    #             log.error('要更新的小说信息不存在！')
    #             return False
    #     return True
    #
    # """ 根据URL更新小说章节页URL """
    # def update_novel_info_chapter_by_url(self, book_url: str, chapter_base_url: str):
    #     if self.novel_info_is_locked_by_url(book_url):
    #         log.info('书籍信息被锁!不可修改!')
    #         return True
    #     if self.novel_info_exist(book_url):  # 小说信息存在，更新
    #         msql = 'UPDATE `novel_info` SET chapter_base_url = "{chapter_base_url}", `update_time`="{update}"\
    #                         WHERE book_url = "{book_url}";' \
    #             .format(chapter_base_url=self._connect.escape_string(str(chapter_base_url)),
    #                     book_url=self._connect.escape_string(book_url),
    #                     update=int(time.time()))
    #         try:
    #             curosr = self._connect.cursor()
    #             curosr.execute(msql)
    #             self._connect.commit()
    #         except Exception as e:
    #             log.error('书籍章节页更新失败：: ' + str(e))
    #             return False
    #         else:
    #             log.error('要更新的小说信息不存在！')
    #             return False
    #     return True
    #
    # """ 根据URL更新小说章节页URL """
    # def update_novel_info_chapter_by_url(self, book_url: str, chapter_base_url: str):
    #     if self.novel_info_is_locked_by_url(book_url):
    #         log.info('书籍信息被锁!不可修改!')
    #         return True
    #     if self.novel_info_exist(book_url):  # 小说信息存在，更新
    #         msql = 'UPDATE `novel_info` SET chapter_base_url = "{chapter_base_url}", `update_time`="{update}"\
    #                         WHERE book_url = "{book_url}";' \
    #             .format(chapter_base_url=self._connect.escape_string(str(chapter_base_url)),
    #                     book_url=self._connect.escape_string(book_url),
    #                     update=int(time.time()))
    #         try:
    #             curosr = self._connect.cursor()
    #             curosr.execute(msql)
    #             self._connect.commit()
    #         except Exception as e:
    #             log.error('书籍章节页更新失败：: ' + str(e))
    #             return False
    #         else:
    #             log.error('要更新的小说信息不存在！')
    #             return False
    #     return True


if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))