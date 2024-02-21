from django.urls import path
from . import views

urlpatterns = [
    path('manageTransaction/', views.transation_api),
]
