from django.urls import path
from . import views

urlpatterns = [
    path('myGoverment/', views.myGoverment_api),
]
