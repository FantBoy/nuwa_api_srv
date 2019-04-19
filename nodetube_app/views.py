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
    # @HttpRequestDecorator
    # def post(self, request):
    #     request_dict = json.loads(request.body)
    #     return self.do(request, request_dict)
    #
    # @HttpRequestDecorator
    # def get(self, request):
    #     request_dict = parse_params(request.GET)
    #     return self.do(request, request_dict)
    #
    # def do(self, request, request_dict):
    def post(self, request):
        return HttpResponse("ok")