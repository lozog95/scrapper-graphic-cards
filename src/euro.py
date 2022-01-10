import scrapy
from html import unescape
import unicodedata
import time
class EuroGCSpider(scrapy.Spider):
    name = 'cards'
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