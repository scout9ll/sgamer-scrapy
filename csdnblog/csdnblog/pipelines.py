# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import re
import os

class CsdnblogPipeline(object):
    def process_item(self, item, spider):
        data = re.findall("http://blog.csdn.net/(.*?)/article/details/(\d*)", item['url'])
        #构造文件名
        filename = data[0][0] + '_' + data[0][1] + '.txt'
        text = "标题: " + item['title'] + "\n博文链接: " + item['url'] + "\n发布时间: " \
                + item['releaseTime'] + "\n\n正文: " + item['article']  #载入TXT中为UTF-8
                  #  windows txt默认为GBK解码，所以使用encoding=utf-8
        with open (filename,"w",encoding='utf-8') as  file_object:
            file_object.write(text)

        print(data)
        return item