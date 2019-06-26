#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
from frame.common.param import *
from frame.xingzuo_parser.com_piaoliang import CMPiaoliangParser


class ParserFactory:
    def get_parser(self, parser_name: str):
        if parser_name in self._parserDict:
            return self._parserDict[parser_name]
    _parserDict = {
        COM_PIAOLIANG_NAME: CMPiaoliangParser(),
    }


_parser = ParserFactory()


def get_parser():
    return _parser
