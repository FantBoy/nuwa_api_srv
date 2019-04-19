from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
# Create your views here.

import logging 
logger = logging.getLogger('django')


class QueryGroupList(View):
    def get(self, request):
        data = [
            {
                "title": "",
                "createdAt": "",
                "owner": "",
                "subDescription": ""
            }
        ]
        return JsonResponse({"data": data})

class EditGroup(View):
    def post(self, request):
        return HttpResponse("ok")