import scrapy
import json
from ..items import InstacrawlItem

class InstagramspiderSpider(scrapy.Spider):
    name = 'instagramspider'
    allowed_domains = ['www.instagram.com']
    start_urls = ['http://www.instagram.com/clementberrurie/?__a=1']

    def __init__(self):
        super(InstaSpider, self).__init__()

    def parse(self, response):

        jsonresponse = json.loads(response.body_as_unicode())

        item = InstacrawlItem()
        item['full_name'] = jsonresponse['user']['full_name']
        item['username']  = jsonresponse['user']['username']
        item['bio']       = jsonresponse['user']['biography']
        item['followers'] = jsonresponse['user']['followed_by']['count']
        item['following'] = jsonresponse['user']['follows']['count']

        print('Init !')

        filename = "crawler.json"
        with open(filename,'w') as f:
            for key,value in item.items() :
                f.write("{%s : %s}" % (key, str(value).encode('utf-8')))
        f.close()

        print('Done !')

        yield item