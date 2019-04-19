from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from nodetube_app.views import Add

app_name = 'nodeTubeAppUrls'
urlpatterns = [
    url(r'add', Add.as_view(), name="add"),
]