#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request

class HtmlDownloader(object):
    def download(self, pg):
        if pg is None and pg.url is None:
            return None
        page = urllib.request.urlopen(pg.url)
        return page.read()


if __name__ == '__main__':
    pass