from django.urls import path
from . import views

urlpatterns = [
    path('groupManagement/', views.managegroup_api),
]
