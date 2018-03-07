# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re
from SGgames.items import SggamesItem
from scrapy import Request


class ShagouSpider(scrapy.Spider):
    name = "shagou"
    allowed_domains = ["bbs.sgamer.com"]
    start_urls = ['https://bbs.sgamer.com/forum-44-1.html']

    def parse(self, response):

        for i in range(5):
            url = 'https://bbs.sgamer.com/forum-44-%d.html' % (i + 1)
            yield Request(url=url, callback=self.get_urls)


    def get_urls(self,response):
        data = response.body  # utf-8字节码bytes型b" "

        soup = BeautifulSoup(data, 'lxml')
        urls = soup.findAll("a", onclick="atarget(this)")
        for url in urls:
            target_url = "https://bbs.sgamer.com/" + url.get("href")

            yield Request(url=target_url, callback=self.get_targeturls)

    def get_targeturls(self, response):
        item = SggamesItem()
        data = response.body  # utf-8字节码bytes型b" "

        soup = BeautifulSoup(data, 'lxml')
        c = soup.findAll("div", id=re.compile("post_[0-9]+"))
        tilte = soup.find("span", id="thread_subject").get_text()
        try:
            next_page = soup.find("a", attrs={"class": "nxt"}).get("href")
        except:
            next_page = None
        for x in c:
            item["tilte"] = tilte
            item['nickname'] = x.find("a", target="_blank").get_text()
            item["rank"] = int(re.findall(r"http://fj2.sgamer.com/attachment/common/.+?/common_(.+?)_usergroup_icon.png", str(x))[0])
            try:
                item["comment"] = x.find("td", id=re.compile("postmessage")).get_text().replace("\n", "").replace("\r", "")
            except:
                item["comment"]="muted"
            yield item
        if next_page is not None:
            yield Request(url="https://bbs.sgamer.com/" + next_page, callback=self.get_targeturls)

