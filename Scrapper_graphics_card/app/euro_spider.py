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
import crochet
#crochet.setup()


class EuroGCSpider(scrapy.Spider):
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'app/euro_output.json'
    }
    name = 'euro_spider'
    #retriving URL parsed as argument to this spider
    def __init__(self, *args, **kwargs): 
      super(EuroGCSpider, self).__init__(*args, **kwargs) 
      self.start_urls = [kwargs.get('start_url')]
      print(self.start_urls)
    
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


def start_scraper(given_url):
    
    #crochet used to run spider from script of non main thread
    crochet.setup()

    #running spider, arachnophobia alert (!)
    runner = CrawlerRunner()
    d = runner.crawl(EuroGCSpider,start_url=given_url)

