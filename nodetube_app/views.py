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
    @HttpRequestDecorator
    def get(self, request):

        group_list = ProgrameGroup.objects.all()
        groups = {}
        if group_list:
            groups = [group.to_dict() for group in group_list]
        return groups, False


class EditGroup(View):

    def getData(self):
        group_list = ProgrameGroup.objects.all()
        groups = {}
        if group_list:
            groups = [group.to_dict() for group in group_list]
        return groups

    def add(self, request, request_dict):
        try:
            result = {"ret": -1, "msg": ""}
            if 'id' in request_dict:
                del request_dict['id']
            new_group = ProgrameGroup(**request_dict)
            new_group.save()
            result['ret'] = 0
        except NuwaApiServerException as e:
            logger.error(e.response_msg)
        except Exception as e:
            logger.error(e)
        finally:
            if -1 == result['ret']:
                return result
            else:
                return self.getData()
    # def get(self, request):
    #     request_dict = request.GET
    #     return self.do(request, request_dict)

    @HttpRequestDecorator
    def post(self, request):
        # antd post的表单数据在body，不在requet.POST
        #request_dict = request.POST.dict()
        request_dict = json.loads(request.body)
        method = request_dict.get('method', None)

        if not method:
            errmsg = "post data do not has mothed: ", json.dump(request_dict)
            logger.error(errmsg)
            return {"ret": -1, "msg": errmsg}
            #raise NuwaApiServerException(PostParamsError)
        del request_dict['method']
        if 'post' == method:
            return self.add(request, request_dict), False