"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app.euro_spider import EuroGCSpider, start_scraper

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
    """Renders the contact page."""
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

    output = start_scraper("test")
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/rtx3060.html',
        {
            'item_list':output,
            'title':'Nvidia RTX 3060',
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
