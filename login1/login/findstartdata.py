from pymongo import MongoClient

class getInstance():
    # #数据库链接开启
    client = MongoClient()
    db = client.Spider_content
    collection = db.user
    # #数据库取值
    # global urls
    # # start_urls = db.user.distinct('start_url')
    # url = db.user.distinct('start_url')
    # # allowed_domains = db.user.distinct('allowed_domains')
    # # username = db.user.distinct('username')
    # # print(allowed_domains[0])
    # # print(start_urls)
    # # # print(username[0])
    # for i in url:
    #     start_urls=i
    #     print(start_urls)
    #
    #
    # global rules_urls
    # rules_url = db.user.distinct('start_url')
    # # s=''.join(rules_url)
    # # print(s)
    # print(rules_url)
    # #
    # # for i in rules_url:
    # #     rules_url = i
    #     print(rules_url)


    global rules_urls
    url = db.user.distinct('start_url')
    rules_url=''.join(url)
    print(rules_url)

