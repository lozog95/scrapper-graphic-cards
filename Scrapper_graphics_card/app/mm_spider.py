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

class MMGCSpider(scrapy.Spider):
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'app/mm_output.json'
    }
    name = 'cards'
    def __init__(self, *args, **kwargs): 
      super(MMGCSpider, self).__init__(*args, **kwargs) 
      self.start_urls = [kwargs.get('start_url')]
      print("URLEEEEE")
      print(self.start_urls)


    def _cleanup_price(self, price):
        price=price.strip()
        price=price.replace('\t', '')
        price=price.replace('\u202f', '')
        price=price.replace('z\u0142', '')
        price=price.replace(' ', '')
        return price

    def _cleanup_name(self, name):
        name = name.strip()
        name = name.replace("  ", "")
        name = name.lstrip("Karta graficzna ")
        return name

    def parse(self, response):
        #
        for card in response.css('div.offers.is-list > div.offer'):
            yield {
                'price': self._cleanup_price(card.css('div.tab.price > div > div > span::text').get()),
                'card': self._cleanup_name(card.css('h2.title::text').get()),
                'link': "https://mediamarkt.pl"+card.css('div.info > a.spark-link::attr("href")').get()
            }
        

        next_page=response.css('a.paging-number::attr("href")').get()
        if next_page is not None and next_page != "/karty-graficzne,typ-chipsetu!geforce-rtx-3060.bhtml":
            yield response.follow(next_page, self.parse)



def mm_start_scraper(given_url):
    
    #crochet used to run spider from script of non main thread
    crochet.setup()
    
    #running spider, arachnophobia alert (!)
    runner = CrawlerRunner()
    #d = runner.crawl(EuroGCSpider,start_url=given_url)
    d = runner.crawl(MMGCSpider, start_url=given_url)

