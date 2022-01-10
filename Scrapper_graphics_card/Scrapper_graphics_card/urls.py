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

    path('rtx3060/', views.rtx3060, name='rtx3060'),
    path('rtx3060/results_euro', views.rtx3060_result, name='rtx3060'),
    path('rtx3060/results_me', views.rtx3060_result, name='rtx3060'),
    path('rtx3060/results_mm', views.rtx3060_result, name='rtx3060'),

    path('rtx3060ti/', views.rtx3060ti, name='rtx3060ti'),
    path('rtx3060ti/results_euro', views.rtx3060ti_result, name='rtx3060ti'),
    path('rtx3060ti/results_me', views.rtx3060ti_result, name='rtx3060ti'),
    path('rtx3060ti/results_mm', views.rtx3060ti_result, name='rtx3060ti'),

    path('rtx3070/', views.rtx3070, name='rtx3070'),
    path('rtx3070/results_euro', views.rtx3070_result, name='rtx3070'),
    path('rtx3070/results_me', views.rtx3070_result, name='rtx3070'),
    path('rtx3070/results_mm', views.rtx3070_result, name='rtx3070'),

    path('rtx3080/', views.rtx3080, name='rtx3080'),
    path('rtx3080/results_euro', views.rtx3080_result, name='rtx3080'),
    path('rtx3080/results_me', views.rtx3080_result, name='rtx3080'),
    path('rtx3080/results_mm', views.rtx3080_result, name='rtx3080'),

    path('rtx3090/', views.rtx3090, name='rtx3090'),
    path('rtx3090/results_euro', views.rtx3090_result, name='rtx3090'),
    path('rtx3090/results_me', views.rtx3090_result, name='rtx3090'),
    path('rtx3090/results_mm', views.rtx3090_result, name='rtx3090'),

    path('xboxseriesx/', views.xboxseriesx, name='xboxseriesx'),
    path('xboxseriesx/results_euro', views.xboxseriesx_result, name='xboxseriesx'),
    path('xboxseriesx/results_me', views.xboxseriesx_result, name='xboxseriesx'),
    path('xboxseriesx/results_mm', views.xboxseriesx_result, name='xboxseriesx'),

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
