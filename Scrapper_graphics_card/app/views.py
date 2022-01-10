"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app.euro_spider import start_scraper
from app.models import clean_json_files, json_reader
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
    given_url = 'https://www.euro.com.pl/karty-graficzne,typ-chipsetu!geforce-rtx-3060.bhtml'

    #starting euro scraper with given URL
    start_scraper(given_url)
    while True:
        time.sleep(1)
        if os.path.exists("app/euro_output.json"):
            break
    return HttpResponseRedirect("/rtx3060/results_euro")

    #assert isinstance(request, HttpRequest)
    """return render(
            request,
            'app/choice_template.html',
            {    
                'title':'Nvidia RTX 3060',
                'year':datetime.now().year,
            }
    )"""
def rtx3060_result(request):
    #reading scraper output files
    output = json_reader()
    assert isinstance(request, HttpRequest)

    #and rendering output files with item list from scrapy
    return render(
        request,
        'app/result_template.html',
        {
            'item_list':output,
            'title':'Nvidia RTX 3060',
            'year':datetime.now().year,
        }
    )

def rtx3060ti(request):
    clean_json_files()
    given_url = 'https://www.euro.com.pl/karty-graficzne,typ-chipsetu!geforce-rtx-3060-ti.bhtml'
    start_scraper(given_url)
    while True:
        time.sleep(1)
        if os.path.exists("app/euro_output.json"):
            break
    return HttpResponseRedirect("/rtx3060ti/results_euro")

def rtx3060ti_result(request):
    output = json_reader()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/result_template.html',
        {
            'item_list':output,
            'title':'Nvidia RTX 3060Ti',
            'year':datetime.now().year,
        }
    )

def rtx3070(request):
    clean_json_files()
    given_url = 'https://www.euro.com.pl/karty-graficzne,typ-chipsetu!geforce-rtx-3070.bhtml'
    start_scraper(given_url)
    while True:
        time.sleep(1)
        if os.path.exists("app/euro_output.json"):
            break
    return HttpResponseRedirect("/rtx3070/results_euro")

def rtx3070_result(request):
    output = json_reader()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/result_template.html',
        {
            'item_list':output,
            'title':'Nvidia RTX 3070',
            'year':datetime.now().year,
        }
    )

def rtx3080(request):
    clean_json_files()
    given_url = 'https://www.euro.com.pl/karty-graficzne,typ-chipsetu!geforce-rtx-3080.bhtml'
    start_scraper(given_url)
    while True:
        time.sleep(1)
        if os.path.exists("app/euro_output.json"):
            break
    return HttpResponseRedirect("/rtx3080/results_euro")

def rtx3080_result(request):
    output = json_reader()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/result_template.html',
        {
            'item_list':output,
            'title':'Nvidia RTX 3080',
            'year':datetime.now().year,
        }
    )

def rtx3090(request):
    clean_json_files()
    given_url = 'https://www.euro.com.pl/karty-graficzne,typ-chipsetu!geforce-rtx-3090.bhtml'
    start_scraper(given_url)
    while True:
        time.sleep(1)
        if os.path.exists("app/euro_output.json"):
            break
    return HttpResponseRedirect("/rtx3090/results_euro")
def rtx3090_result(request):
    output = json_reader()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/result_template.html',
        {
            'item_list':output,
            'title':'Nvidia RTX 3090',
            'year':datetime.now().year,
        }
    )

def xboxseriesx(request):
    if os.path.exists("app/euro_output.json"):
        os.remove("app/euro_output.json")
    given_url = 'https://www.euro.com.pl/konsole-xbox-series.bhtml'
    start_scraper(given_url)
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/choice_template.html',
            {   
                'title':'Xbox Series X',
                'year':datetime.now().year,
            }
    )
def xboxseriesx_result(request):
    output = json_reader()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/result_template.html',
        {
            'item_list':output,
            'title':'Xbox Series X',
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
