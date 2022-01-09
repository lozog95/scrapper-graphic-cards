import scrapy
from html import unescape
import unicodedata
import time

class EuroGCSpider(scrapy.Spider):
    name = 'cards'
    start_urls = [
        'https://www.euro.com.pl/karty-graficzne.bhtml',
    ]

    def _cleanup_price(self, price):
        price=price.strip()
        price=price.replace('\t', '')
        price=price.replace('z\u0142', '')
        price=price.replace(' ', '')
        return price

    def _cleanup_name(self, name):
        name=name.strip()
        name=name.replace("\u00ae","")
        return name

    def parse(self, response):
        for card in response.css('div.product-for-list'):
            yield {
                'price': self._cleanup_price(unicodedata.normalize('NFKC', unescape(card.css('div.price-normal::text').get()))),
                'card': self._cleanup_name(unicodedata.normalize('NFKC', unescape(card.css('span.attribute-value::text').get()))),
            }
        

        next_page=response.css('a.paging-number::attr("href")').get()
        if next_page is not None and next_page != "/karty-graficzne.bhtml":
            yield response.follow(next_page, self.parse)