from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [

   path('', views.index, name = 'events-page'),
    path('about/', views.about, name = 'events-about'),
]
