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
class EuroGCSpider(scrapy.Spider):
    
    name = 'euro_spider'
    #retriving URL parsed as argument to this spider
    def __init__(self, model, *args, **kwargs): 
      super(EuroGCSpider, self).__init__(*args, **kwargs) 
      self.start_urls = [kwargs.get('start_url')]
      self.model = model
    
    #this function cleans price from weird characters scraped
    def _cleanup_price(self, price):
        price=price.strip()
        price=price.replace('\t', '')
        price=price.replace('z\u0142', '')
        price=price.replace(' ', '')
        return price

    #and same story for name
    def _cleanup_name(self, name):
        name = name.lstrip("karta graficzna ")
        return name

    #finaly parsing the response and retrieving attributes
    def parse(self, response):
        for card in response.css('div.product-for-list'):
            yield {
                'price': self._cleanup_price(unicodedata.normalize('NFKC', unescape(card.css('div.price-normal::text').get()))),
                'card': self._cleanup_name(card.css('a.js-save-keyword > img::attr("alt")').get()),
                'link': "https://euro.com.pl"+card.css('a.js-save-keyword::attr("href")').get()
            }
        

        next_page=response.css('a.paging-number::attr("href")').get()
        if next_page is not None and next_page != "/karty-graficzne,typ-chipsetu!geforce-rtx-3060.bhtml":
            yield response.follow(next_page, self.parse)


def euro_start_scraper(given_url, model):
    
    #crochet used to run spider from script of non main thread
    crochet.setup()
    s = get_project_settings()
    dt=datetime.now().strftime('%Y%m%d')

    s.update({
        'FEED_FORMAT': 'json',
        'FEED_URI': f"app/euro_{dt}_{model}.json"
    })
    #running spider, arachnophobia alert (!)
    runner = CrawlerRunner(settings=s)
    d = runner.crawl(EuroGCSpider,start_url=given_url, model=model)


