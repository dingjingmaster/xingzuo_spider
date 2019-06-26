#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
import time
from urllib.parse import unquote


class Util:
    @staticmethod
    def check_url (url: str, base_url: str) -> str:
        if not url.startswith("https://") and url.startswith("http://"):
            url = base_url + '/' + url
        try:
            url = unquote(url, 'utf8')
        except Exception:
            url = ''
        return url

    @staticmethod
    def time_str_stamp (time_str, fmt: str) -> int:
        tm = 0
        try:
            tm = time.mktime(time.strptime(time_str, fmt))

        except:
            pass
        return tm

    @staticmethod
    def valid (field) -> bool:
        if (None is field) or ('' == field.strip()):
            return False
        return True
