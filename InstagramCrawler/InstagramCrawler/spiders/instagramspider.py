# -*- coding: utf-8 -*-
import scrapy
#import json
#from items.py import InstagramcrawlerItem

class InstagramspiderSpider(scrapy.Spider):
    name = 'instagramspider'
    allowed_domains = ['www.instagram.com']
    start_urls = ['http://www.instagram.com/clementberrurie/?__a=1']

    def parse(self, response):
        print('________test________')

        #Le code qu'on a fait pour le moment logiquement fonctionnel
        '''
        items=[]
        jsonresponse = json.loads(response.body_as_unicode())
        #for key, value in jsonresponse['logging_page_id']:
        item = Infos()
            #print value
        item['username'] = jsonresponse['user']['username']
        item['followers'] = jsonresponse['user']['follows']['count']
        items.append(item)
        filename = "crawler.json"
        with open(filename,'wb') as f:
            f.write(items)
        self.log('saved file %s' % filename)
        '''

