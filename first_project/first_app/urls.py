from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from first_app import views


urlpatterns= [
    url(r'^$',views.index,name='index'),
]
