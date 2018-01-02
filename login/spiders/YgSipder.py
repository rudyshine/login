#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule

from login.items import LoginItem


class login(CrawlSpider) :
    """继承自CrawlSpider，实现自动爬取的爬虫。"""

    name = "e_login"
    print("aaaa ===========1")
    allowed_domains =['ygsoft.com']
    print("aaaa ===========1")
    # start_urls = ["http://www.newsmth.net/mainpage.html",]
    # start_urls = ["http://bonsaiden.github.io/JavaScript-Garden/zh/", ]
    # start_urls = ["http://www.ygsoft.com/",]

    # start_urls = None
    print("aaaa ===========1")
    def __init__(self,start_urls, *args, **kwargs):
        super(login, self).__init__(*args, **kwargs)
        self.start_urls = [start_urls]cd
        # self.allowed_domains = [start_urls.strip('http:\/\/www.')]

        print(self.start_urls)
        # print(self.allowed_domains)
        print(self.start_urls)

    ###Rule对象定义了爬取网站的特定行为。其第一个参数Link Extractor  object描述了从每个爬取网页中提取链接的方式，callback参数用于处理LinkExtractor提取的链接
    rules = [
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@href]')),callback='parse_page',follow=True)]
    print("aaaa ===========3")
    ##无登录
    def parse_page(self, response):
        items = []
        problem = Selector(response)
        second_url = problem.xpath('//a/@href').extract()
        print("aaaa ===========2")
        # for j in range(0, len(second_url)):
        item = LoginItem()
            # item['second_url'] = second_url[j]
        item['final_url']=response.url
            # print(item['final_url'])
            # items.append(item)
        # for item in items:
        item['head'] =problem.xpath('/html/head/title/text()').extract()

        content = ""
        content_list = problem.xpath('/html/body/*').extract()
        for content_one in content_list:
            content += content_one
        reg = re.compile('<[^>]*>')
        content = reg.sub('', content)
        item['content'] = content

        content = ""
        # content_list= problem.xpath('/html/body').extract()
        content_list = problem.xpath("string(/html/body)").extract()
        for content_one in content_list:
            content += content_one
        item['content'] = content
        yield item
