from django.urls import path
from . import views

urlpatterns = [
    path('myFarm/', views.myFarm_api),
]
