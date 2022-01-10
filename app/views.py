﻿"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app.euro_spider import euro_start_scraper
from app.me_spider import me_start_scraper
from app.mm_spider import mm_start_scraper
from app.models import clean_json_files, json_reader, output_lists
import time
import os
from django.http import HttpResponseRedirect


def home(request):
    clean_json_files()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Strona główna',
            'year':datetime.now().year,
        }
    )

def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 
        'app/contact.html',
        {
            'title':'Kontakt',
            'message':'',
            'year':datetime.now().year,
        }
    )

def rtx3060(request):
    #cleaning previous json file if it exist
    clean_json_files()
    #static url for this specific card model
    euro_url = 'https://www.euro.com.pl/karty-graficzne,typ-chipsetu!geforce-rtx-3060.bhtml'
    me_url = 'https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/geforce-rtx_tak/model_geforce-rtx-3060'
    mm_url = 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/czesci-komputerowe/karty-graficzne./uklad-graficzny=geforce-rtx-3060'
    mm_start_scraper(mm_url)
    me_start_scraper(me_url)
    euro_start_scraper(euro_url)
    #euro_start_scraper(given_url)
    while True:
        time.sleep(1)
        if os.path.exists("app/mm_output.json"):
            break
    return HttpResponseRedirect("/rtx3060/results")

    #assert isinstance(request, HttpRequest)
    """return render(
            request,
            'app/choice_template.html',
            {    
                'title':'Nvidia RTX 3060',
                'year':datetime.now().year,
            }
    )"""

def rtx3060ti(request):
    clean_json_files()
    euro_url = 'https://www.euro.com.pl/karty-graficzne,typ-chipsetu!geforce-rtx-3060-ti.bhtml'
    me_url = 'https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/geforce-rtx_tak/model_geforce-rtx-3060-ti'
    mm_url = 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/czesci-komputerowe/karty-graficzne./uklad-graficzny=geforce-rtx-3060-ti'
    mm_start_scraper(mm_url)
    #starting euro scraper with given URL
    me_start_scraper(me_url)
    euro_start_scraper(euro_url)
    while True:
        time.sleep(1)
        if os.path.exists("app/euro_output.json"):
            break
    return HttpResponseRedirect("/rtx3060ti/results")

def rtx3070(request):
    clean_json_files()
    euro_url = 'https://www.euro.com.pl/karty-graficzne,typ-chipsetu!geforce-rtx-3070.bhtml'
    me_url = 'https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/geforce-rtx_tak/model_geforce-rtx-3070'
    mm_url = 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/czesci-komputerowe/karty-graficzne./uklad-graficzny=geforce-rtx-3070'
    mm_start_scraper(mm_url)
    me_start_scraper(me_url)
    euro_start_scraper(euro_url)
    while True:
        time.sleep(1)
        if os.path.exists("app/euro_output.json"):
            break
    return HttpResponseRedirect("/rtx3070/results")

def rtx3080(request):
    clean_json_files()
    euro_url = 'https://www.euro.com.pl/karty-graficzne,typ-chipsetu!geforce-rtx-3080.bhtml'
    me_url = 'https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/geforce-rtx_tak/model_geforce-rtx-3080'
    mm_url = 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/czesci-komputerowe/karty-graficzne./uklad-graficzny=geforce-rtx-3080'
    mm_start_scraper(mm_url)
    me_start_scraper(me_url)
    euro_start_scraper(euro_url)

    while True:
        time.sleep(1)
        if os.path.exists("app/euro_output.json"):
            break
    return HttpResponseRedirect("/rtx3080/results")


def rtx3090(request):
    clean_json_files()
    euro_url = 'https://www.euro.com.pl/karty-graficzne,typ-chipsetu!geforce-rtx-3090.bhtml'
    me_url = 'https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/geforce-rtx_tak/model_geforce-rtx-3090'
    mm_url = 'https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/czesci-komputerowe/karty-graficzne./uklad-graficzny=geforce-rtx-3090'
    mm_start_scraper(mm_url)
    me_start_scraper(me_url)
    euro_start_scraper(euro_url)
    while True:
        time.sleep(1)
        if os.path.exists("app/euro_output.json"):
            break
    return HttpResponseRedirect("/rtx3090/results", )

def result_page(request):
    output = output_lists()
    #print(output)
    #output.sort(key=lambda x: x['price'], reverse=False)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/result_template.html',
        {
            'title': "Wyniki wyszukiwania",
            'item_list':output,
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'O nas',
            'message':'Opis strony',
            'year':datetime.now().year,
        }
    )