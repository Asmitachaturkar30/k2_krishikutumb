from django.urls import path
from . import views

urlpatterns = [
    path('myFinance/', views.myFinance_api),
]
