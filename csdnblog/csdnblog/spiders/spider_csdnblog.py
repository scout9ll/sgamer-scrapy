# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import scrapy
import re
from scrapy import Request
from csdnblog.items import CsdnblogItem

class SpiderCsdnblogSpider(scrapy.Spider):
    name = 'spider_csdnblog'
    allowed_domains = ['csdn.net']
    start_urls = ['http://blog.csdn.net/oscer2016/article/details/78007472']

    def parse(self, response):
        item = CsdnblogItem()

        # 新版主题博客数据抽取
        item['url'] = response.url
        item['title'] = response.xpath('//h1[@class="csdn_top"]/text()').extract()[0]
        item['releaseTime'] = response.xpath('//span[@class="time"]/text()').extract()[0]
        item['readnum'] = response.xpath('//button[@class="btn-noborder"]/span/text()').extract()[0]
        data = response.xpath('//div[@class="markdown_views"]')
        item['article'] = data.xpath('string(.)').extract()[0]

        # 将数据传入pipelines.py，然后写入文件
        yield item