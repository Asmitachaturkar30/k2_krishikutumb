from django.urls import path
from . import views

urlpatterns = [
    path('manageBucketS3/', views.manageBucket_api),
]
