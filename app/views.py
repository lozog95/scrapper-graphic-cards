"""
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
import app.utils as utils
from django.http import HttpResponseRedirect
from django.urls import resolve
import ast
import json


def home(request):
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

def refresh_page(request, model):
    print("Model in refresh page")
    print(model)
    clean_json_files(model)
    return HttpResponseRedirect(f"/result/{model}")

def render_page(request, model):

   # print(utils.lookup_file(model))
    print("Model in render page is:")
    print(model)
    if os.path.exists(os.path.join("app", utils.lookup_file(model))):
        print("JSON already exists")
        return HttpResponseRedirect(f"/result/{model}/results")
    if model=="rtx3060ti":
        site_model="3060-ti"
    else:
        site_model= model[4:]
        print(site_model)
    #static url for this specific card model
    #euro_url = 'https://www.euro.com.pl/karty-graficzne,typ-chipsetu!geforce-rtx-3060.bhtml'
    me_url = f"https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/geforce-rtx_tak/model_geforce-rtx-{site_model}"
    mm_url = f"https://mediamarkt.pl/komputery-i-tablety/akcesoria-komputerowe/czesci-komputerowe/karty-graficzne./uklad-graficzny=geforce-rtx-{site_model}"
    print("Media mark url to be checked")
    print(mm_url)
    mm_start_scraper(mm_url,model)
    me_start_scraper(me_url, model)
    #euro_start_scraper(euro_url, model)
    
    while True:
        time.sleep(1)
        if os.path.exists(os.path.join("app",utils.lookup_file(model, shop="me"))):
            break
    #time.sleep(1)
    output = output_lists(model)
    #print(output)
    #output.sort(key=lambda x: x['price'], reverse=False)

    return HttpResponseRedirect(f"/result/{model}/results")

def result_page(request, model):
    global_path = os.path.join("app", utils.lookup_file(model))
    if os.path.exists(global_path):
        print("JSON already exists RESULTS PAGE")
        output = json.loads(open(global_path).readlines()[0])
    else:
        output = output_lists(model)
    #print(output)
    #output.sort(key=lambda x: x['price'], reverse=False)
    historical_data=utils.get_model_history(model)
    return render(
        request,
        'app/result_template.html',
        {
            'average':output["average"],
            'title': "Wyniki wyszukiwania",
            'item_list':output["results"],
            'history_list': historical_data["prices"],
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
