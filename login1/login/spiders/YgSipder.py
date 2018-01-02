#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from login.items import LoginItem


class login(CrawlSpider) :
    """继承自CrawlSpider，实现自动爬取的爬虫。"""

    name = "nologin"
    ## allowed_domains=['ecp.ygsoft.com']
    # # start_urls = ["http://ecp.ygsoft.com:9080/grm/ecosphere/cloudplatform/index.html",]

    def __init__(self,start_urls, *args, **kwargs):
        super(login, self).__init__(*args, **kwargs)
        self.start_urls = [start_urls]
        self.url=start_urls
        # print(self.url)
        reg = r'^https?:\/\/([a-z0-9\-\.]+)[\/\?]?'
        m = re.match(reg, start_urls)
        self.allowed_domains = [m.groups()[0] if m else '']
        # print("aaaa ===========")
        # print(self.start_urls)
        # print(self.allowed_domains)


    ###Rule对象定义了爬取网站的特定行为。其第一个参数Link Extractor  object描述了从每个爬取网页中提取链接的方式，callback参数用于处理LinkExtractor提取的链接  /html/body/div[1]/div/div[1]/div/ul/li[1]/a

    # rules = (Rule(LinkExtractor(allow=('http://mup.ygsoft.com:8080/web/site/+.*',)), callback='parse_page', follow=True),)#取值
    rules = [Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@href]')), callback='parse_page', follow=True)]

    ##无登录
    def parse_page(self, response):
        items = []
        problem = Selector(response)
        item = LoginItem()
        item['final_url']=response.url
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


    # def parse_page(self, response):
    #     items = []
    #     problem = Selector(response)
    #     second_url = problem.xpath('//a/@href').extract()
    #     for j in range(0, len(second_url)):
    #         item = LoginItem()
    #         item['second_url'] = second_url[j]
    #         # print(item['second_url'])
    #         items.append(item)
    #     for item in items:
    #         yield Request(url=self.url+ item['second_url'], callback=self.parse_dir_contents)
    #         # yield item
    #
    #
    # def parse_dir_contents(self, response):
    #     problem = Selector(response)
    #     item = LoginItem()
    #     item['final_url'] = response.url
    #     item['head']= problem.xpath('/html/head/title/text()').extract()
    #
    #
    #     content = ""
    #     content_list = problem.xpath('/html/body/*').extract()
    #     for content_one in content_list:
    #         content += content_one
    #     reg = re.compile('<[^>]*>')
    #     content = reg.sub('', content)
    #     item['content'] = content.strip('\r\n')
    #
    #     yield item
