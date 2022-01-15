import scrapy
from html import unescape
import unicodedata
import time
import os
import json
 
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import crochet
from datetime import datetime
 
 
class MeGCSpider(scrapy.Spider):
  
    name = 'cards'
    def __init__(self, model, *args, **kwargs): 
        super(MeGCSpider, self).__init__(*args, **kwargs) 
        self.start_urls = [kwargs.get('start_url')]
        #print(self.start_urls)
        self.model=model
        print("W konst ME")
        print(self.model)
        print(self.start_urls)
 
 
 
    def _cleanup_name(self, name):
        name = name.strip()
        name = name.replace("  ", "")
        name = name.lstrip("Karta graficzna ")
        return name
 
    def _cleanup_price(self, price):
        #try:
            price=price.strip()
            price=price.replace('\t', '')
            price=price.replace('\u202f', '')
            price=price.replace('z\u0142', '')
            price=price.replace(' ', '')
        #except:
         #   price = "not available"
            return price
 
    def parse(self, response):
        #
        for card in response.css('#section_list-items > div > span'):
            price = card.css('div > div.dynamic-content > div > div.price-box > div.prices-section > div > div > span::text').get()
            if price:
                yield {
                    'price': self._cleanup_price(price),
                    'card': self._cleanup_name(card.css('div.box > h2 > a::text').get()),
                    'link': "https://mediaexpert.pl"+card.css('a.spark-link::attr("href")').get()
                }
        
 
        next_page=response.css('a.paging-number::attr("href")').get()
        if next_page is not None and next_page != "/karty-graficzne,typ-chipsetu!geforce-rtx-3060.bhtml":
            yield response.follow(next_page, self.parse)
 
 
def me_start_scraper(given_url, model):
    
    #crochet used to run spider from script of non main thread
    crochet.setup()
    s = get_project_settings()
    dt=datetime.now().strftime('%Y%m%d')
 
    s.update({
        'FEED_FORMAT': 'json',
        'FEED_URI': f"app/me_{dt}_{model}.json"
    })
 
    #running spider, arachnophobia alert (!)
    runner = CrawlerRunner(settings=s)
   # d = runner.crawl(EuroGCSpider,start_url=given_url)
    d = runner.crawl(MeGCSpider,start_url=given_url, model=model)