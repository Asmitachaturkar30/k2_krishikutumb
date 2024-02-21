from django.urls import path
from . import views

urlpatterns = [
    path('managek2App/', views.managek2App_api),
]
