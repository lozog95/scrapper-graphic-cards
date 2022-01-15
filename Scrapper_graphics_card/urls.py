"""
Definition of urls for Scrapper_graphics_card.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    
    path('result/<str:model>/refresh', views.refresh_page, name='model_render'),

    path('result/<str:model>/', views.render_page, name='model_render'),
    path('result/<str:model>/results', views.result_page, name='model_results'),

    # path('rtx3060/', views.render_page, kwargs={'model': 'rtx3060'}, name='rtx3060'),
    # path('rtx3060/results', views.result_page, kwargs={'model': 'rtx3060'}, name='rtx3060'),

    # path('rtx3060ti/', views.render_page, kwargs={'model': 'rtx3060ti'}, name='rtx3060ti'),
    # path('rtx3060ti/results', views.result_page, kwargs={'model': 'rtx3060ti'}, name='rtx3060ti'),



    # path('rtx3060ti/', views.rtx3060ti, name='rtx3060ti'),
    # path('rtx3060ti/results', views.result_page, kwargs={'model': '3060ti'}, name='rtx3060ti'),


    # path('rtx3070/', views.rtx3070, name='rtx3070'),
    # path('rtx3070/results', views.result_page, name='rtx3070'),


    # path('rtx3080/', views.rtx3080, name='rtx3080'),
    # path('rtx3080/results', views.result_page, name='rtx3080'),


    # path('rtx3090/', views.rtx3090, name='rtx3090'),
    # path('rtx3090/results', views.result_page, name='results'),



    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
