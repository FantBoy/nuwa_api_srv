from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from common.DecoratorTools.HttpRequest import HttpRequestDecorator
from common.ErrorModule.ErrorException import NuwaApiServerException
from common.ErrorModule.ErrorCode import *
from models.models import ProgrameGroup
import json
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
        groups = {}
        if group_list:
            groups = [group.to_dict() for group in group_list]

        return JsonResponse(groups)

class EditGroup(View):

    def add(self, request, request_dict):
        try:
            result = {"ret": 0, "msg": ""}
            if 'id' in request_dict:
                del request_dict['id']
            new_group = ProgrameGroup(**request_dict)
            new_group.save()
        except NuwaApiServerException as e:
            logger.error(e.response_msg)
        except Exception as e:
            logger.error(e)
        finally:
            return result
    # def get(self, request):
    #     request_dict = request.GET
    #     return self.do(request, request_dict)

    @HttpRequestDecorator
    def post(self, request):
        request_dict = request.POST.dict()
        method = request_dict.get('method', None)

        if not method:
            errmsg = "post data do net has mothed: ", json.dump(request_dict)
            logger.error(errmsg)
            return {"ret": -1, "msg": errmsg}
            #raise NuwaApiServerException(PostParamsError)
        del request_dict['method']
        if 'post' == method:
            return self.add(request, request_dict)