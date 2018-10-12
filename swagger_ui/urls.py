

from .views import yaml_to_html

try:
    from django.urls import path

    urlpatterns = [
        path('api-doc/', yaml_to_html, name="api-doc"),
    ]
except:
    from django.conf.urls import  url

    urlpatterns = [
        url(r'^api-doc/', yaml_to_html, name="api-doc"),
    ]
