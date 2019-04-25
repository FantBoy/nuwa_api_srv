from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from common.DecoratorTools.HttpRequest import HttpRequestDecorator
from common.ErrorModule.ErrorException import AbcmouseWeChatServerException
from models.models import ProgrameGroup

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
        print(request.GET.get('name'))

        group_list = ProgrameGroup.objects.all()
        groups = [group.to_dict() for group in group_list]
        return JsonResponse(groups)

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