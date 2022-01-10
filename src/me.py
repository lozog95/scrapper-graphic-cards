import scrapy
from html import unescape
import unicodedata


class MeGCSpider(scrapy.Spider):
    name = 'cards'
    start_urls = [
        'https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/geforce-rtx_tak/model_geforce-rtx-3060.geforce-rtx-3060-ti',
    ]

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
        for card in response.css('#section_list-items > div > span'):
            yield {
                'price': self._cleanup_price(card.css('div > div.dynamic-content > div > div.price-box > div.prices-section > div > div > span::text').get()),
                'card': self._cleanup_name(card.css('div.box > h2 > a::text').get()),
                'link': "https://mediaexpert.pl"+card.css('a.spark-link::attr("href")').get()
            }
        

        next_page=response.css('a.paging-number::attr("href")').get()
        if next_page is not None and next_page != "/karty-graficzne,typ-chipsetu!geforce-rtx-3060.bhtml":
            yield response.follow(next_page, self.parse)