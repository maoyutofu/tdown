#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class UrlManager(object):
    def __init__(self):
        self.new_pages = list()
        self.old_urls = list()

    def add_new_page(self, root_page):
        if root_page is None:
            return None
        if root_page not in self.new_pages and root_page not in self.old_urls:
            self.new_pages.append(root_page)

    def add_new_pages(self, new_pages):
        if new_pages is None or len(new_pages) == 0:
            return
        for pg in new_pages:
            self.add_new_page(pg)

    def has_new_page(self):
        return len(self.new_pages) != 0

    def get_new_page(self):
        if len(self.new_pages) == 0:
            return None
        new_page = self.new_pages.pop(0)
        self.old_urls.append(new_page)
        return new_page

if __name__ == '__main__':
    pass