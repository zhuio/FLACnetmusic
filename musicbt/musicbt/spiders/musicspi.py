# -*- coding: utf-8 -*-
import scrapy
import re
import os
from ..playlist import PlayList
from ..items import MusicbtItem

class MusicspiSpider(scrapy.Spider):
    name = 'musicspi'
    allowed_domains = ['bt.com']
    print('输入网易云音乐歌单地址')
    p = PlayList(url=input())
    p.generate()
    list = p.song_name
    slist = []
    for i in range(len(list)):
        slist.append('https://thepiratebay.org/search/%s/0/99/100' % list[i])
    start_urls = ['%s' % i for i in slist]
    # print(start_urls[0])
    def parse(self, response):
        item = MusicbtItem()
        txt = str(response.xpath('//a[@title="Download this torrent using magnet"]').extract())
        btls = re.findall(r'href="(.*?)" title',txt)
        for i in range(len(btls)):
            flag = re.findall(r'FLAC',btls[i])
            if len(flag) != 0:
                item['bt_url'] = [btls[i]]
            else:
                print(btls[i])
        yield item
