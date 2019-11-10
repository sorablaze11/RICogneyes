from django.urls import path
from  . import views

urlpatterns = [
    path('', views.clickImage),
    path('getAudio', views.getAudio),
    path('getNews', views.getNews),
    path('getSOS', views.getSOS),
    path('getOCR', views.getOCR)
]
