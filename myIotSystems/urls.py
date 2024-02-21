from django.urls import path
from . import views

urlpatterns = [
    path('myIotSystems/', views.myIotSystems_api),
]
