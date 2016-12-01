#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from spider import html_parser,html_downloader,url_manager,page

def log(msg):
    print(msg)

class TxtDown(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()

    def output(self, file, root_page):
        file.write(root_page.title)
        file.write('\n')
        if root_page.content is not None:
            file.write(root_page.content)
        file.write('\n\n')

    def craw(self, root_page):
        self.urls.add_new_page(root_page)
        try:
            new_page = self.urls.get_new_page()
            new_page.content = self.downloader.download(new_page)
            new_pages = self.parser.parse_index(new_page)
            self.urls.add_new_pages(new_pages)
            file = open('%s.txt' % root_page.title, 'a', encoding='utf-8')
            new_page.content = None
            self.output(file, new_page)
            log("%s..........................................ok" %new_page.title)
            while self.urls.has_new_page():
                new_page = self.urls.get_new_page()
                html_content = self.downloader.download(new_page)
                new_page.content = self.parser.get_txt(html_content)
                self.output(file, new_page)
                log("%s..........................................ok" %new_page.title)
        except Exception as e:
            print(e)
        finally:
            file.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)
    root_title = sys.argv[1]
    root_url = sys.argv[2]
    root_page = page.Page(root_title, root_url)
    tdown = TxtDown()
    tdown.craw(root_page)