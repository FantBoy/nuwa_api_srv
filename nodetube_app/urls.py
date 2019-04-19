from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from nodetube_app.views import QueryGroupList

app_name = 'nodeTubeAppUrls'
urlpatterns = [
    url(r'querygrouplist', QueryGroupList.as_view(), name="querygrouplist"),
]