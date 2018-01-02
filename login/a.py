#
# # def getInstance():
# #     global c
# #     c = 6
# #     return c
# from pymongo import MongoClient
# from scrapy.spiders import CrawlSpider
#
# class login(CrawlSpider) :
#     # #数据库链接开启
#     client = MongoClient()
#     db = client.Spider_content
#     collection = db.user
#
#
#     name = "e_login"
#     allowed_domains = ["newsmth.net"]
#     # start_urls =webserver.success()
#     # print(start_urls)
#     # # start_urls = [
#     # #     "http://www.newsmth.net/mainpage.html", #取值,
#     # # ]
#
#     # #数据库取值
#     # start_urls=list(db.user.distinct('start_url'))
#     allowed_domains=list(db.user.distinct('allowed_domains'))
#     # start_urls = list(db.user.find())
#     print(allowed_domains)
#     # print(list(collection.find({"id":1}) ))
#     # for data in collection.find({"id": "1"}):
#     #     print(data)



# a = 'http:\\www.baidu.com'
# a.strip('http:\\')
# print(a)
#
# import re
# b = '//item.jd.com/2942458.html'
# reg = re.compile('s/(\/.*\.html)$//')
# reg.sub('',b )
# print(reg.sub('',b ))

# import re
# b = '//item.jd.com/2942458.html'
# reg = re.compile(r'//[a-zA-Z].[a-zA-Z].[a-zA-Z]/.[a-zA-Z]')
# reg.sub('',b )
# print(reg.sub('',b ))

# a = 'http:\\www.baidu.com'
# a = a.strip('http:\\')
# print(a)

# url = 'http:\\www.baidu.com'
# allowed_domains = url.strip('http:\\www.')
# print(allowed_domains)

# from scrapy.spiders import CrawlSpider, Rule
# class login(CrawlSpider) :
#  url='21'
#  def __init__(self, start_urls, *args, **kwargs):
#     super(login, self).__init__(*args, **kwargs)
#     self.start_urls = "http://www.ygsoft.com/"
#     url=self.start_urls
#     # return start_urls
#     def getstarturl():
#         return self.start_urls
#         # print(self.start_urls)
#
#
#  print(url)
#  url = __init__()
#  allowed_domains = url.strip('http:\\www.')

from bs4 import BeautifulSoup
from urllib import request
import re

url='https://sale.jd.com/act/GrZjoT7UQWCn.html'
html=request.urlopen(url).read()
soup=BeautifulSoup(html,"lxml")
for link in soup.find_all('a'):
    print(link.get('href'))