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

runner = CrawlerRunner()

class EuroGCSpider(scrapy.Spider):
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'app/output.json'
    }
    name = 'euro_spider'
    start_urls = [
        'https://www.euro.com.pl/karty-graficzne,typ-chipsetu!geforce-rtx-3060.bhtml',
    ]

    def _cleanup_price(self, price):
        price=price.strip()
        price=price.replace('\t', '')
        price=price.replace('z\u0142', '')
        price=price.replace(' ', '')
        return price

    def _cleanup_name(self, name):
        name = name.lstrip("karta graficzna ")
        return name

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


def start_scraper(url):
    #dirty workaround for now
    if os.path.exists("app/output.json"):
        os.remove("app/output.json")

    #running spider, arachnophobia alert
    d = runner.crawl(EuroGCSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


    with open("app/output.json") as w:
        output = json.loads(w.read())
    return output