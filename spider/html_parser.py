#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.parse
import collections
from spider import page

from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse_index(self, pg):
        if pg is None or pg.content is None:
            return None
        soup = BeautifulSoup(pg.content, 'html.parser', from_encoding='utf-8')
        new_pages = self._get_index_urls(pg, soup)
        return new_pages

    def _get_index_urls(self, pg, soup):
        new_pages = list()
        for a in soup.find('table', class_='a').find_all('a'):
            href = urllib.parse.urljoin(pg.url, a.get('href'))
            title = a.get_text()
            pg = page.Page(title, href)
            new_pages.append(pg)
        return new_pages

    def get_txt(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        txt_content = soup.find(id='content').get_text()
        return txt_content



if __name__ == '__main__':
    pass