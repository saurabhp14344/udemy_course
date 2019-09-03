from django.contrib import admin
from django.urls import path
from profile_api import views

urlpatterns = [
    path('user_info', views.HelloApi.as_view())
]
