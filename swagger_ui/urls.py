
from django.contrib import admin
from django.urls import path

from .views import yaml_to_html

urlpatterns = [
    path('api-doc/', yaml_to_html),
]
