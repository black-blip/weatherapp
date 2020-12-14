from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('search/',views.search,name='search')    
]

