from django.urls import path
from  . import views

urlpatterns = [
    path('api/upload/', views.clickImage),
    path('api/upload/getDetails', views.getDetails)
]
