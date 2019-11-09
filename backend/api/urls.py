from django.urls import path
from  . import views

urlpatterns = [
    path('', views.clickImage),
    path('getAudio', views.getAudio)
]
