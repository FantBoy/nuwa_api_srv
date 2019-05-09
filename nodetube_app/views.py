from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from common.DecoratorTools.HttpRequest import HttpRequestDecorator
from common.ErrorModule.ErrorException import NuwaApiServerException
from common.ErrorModule.ErrorCode import *
from models.models import ProgrameGroup, Device
import json
# Create your views here.

import logging 
logger = logging.getLogger('django')

class QueryGroupList(View):
    @HttpRequestDecorator
    def get(self, request):

        group_list = ProgrameGroup.objects.all()
        groups = []
        if group_list:
            groups = [group.to_dict() for group in group_list]
        return groups, False

class EditGroup(View):

    def getData(self):
        group_list = ProgrameGroup.objects.all()
        groups = []
        if group_list:
            groups = [group.to_dict() for group in group_list]
        return groups

    def add(self, request_dict):
        result = {"ret": -1, "msg": ""}
        try:

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

    def delete(self, id, request_dict):
        result = {"ret": -1, "msg": ""}
        try:
            group = ProgrameGroup.objects.get(id=id)
            group.delete()
            result['ret'] = 0
        except NuwaApiServerException as e:
            logger.error(e.response_msg)
        except ObjectDoesNotExist as e:
            result['msg'] = """this group id {} is not exists in group_list""".format(id)
            logger.error(result['msg'])
        except Exception as e:
            logger.error(e)
        finally:
            if -1 == result['ret']:
                return result
            else:
                return self.getData()

    def update(self, id, request_dict):
        result = {"ret": -1, "msg": ""}
        try:

            group = ProgrameGroup.objects.get(id=id)
            group.group_name = request_dict['group_name']
            group.desc = request_dict['desc']
            # group.modify_time = request_dict['modify_time'] #column设置了自动更新时间
            group.save()
            result['ret'] = 0
        except NuwaApiServerException as e:
            logger.error(e.response_msg)
        except ObjectDoesNotExist as e:
            result['msg'] = """this group id {} is not exists in group_list""".format(id)
            logger.error(result['msg'])
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
        print(request.body)
        request_dict = json.loads(request.body)
        method = request_dict.get('method', None)
        id = request_dict.get('id', None)

        if not method or None == id:
            errmsg = """post data do not has mothed or id: {}""".format(json.dumps(request_dict))
            logger.error(errmsg)
            return {"ret": -1, "msg": errmsg}, True

        del request_dict['method']
        del request_dict['id']

        if 'post' == method:
            return self.add(request_dict), False
        elif 'delete' == method:
            return self.delete(id, request_dict), False
        elif 'update' == method:
            return self.update(id, request_dict), False

class QueryDeviceList(View):
    @HttpRequestDecorator
    def get(self, request):

        device_list = Device.objects.all()
        devices = []
        if device_list:
            for device in device_list:
                person = device.owner

                device_dict = device.to_dict()
                device_dict['owner'] = person.name
                device_dict['group'] = device.group.group_name
                # device_dict['status'] = device.get_status_display()
                devices.append(device_dict)
        pagination = {
            "total": 1,
            "pageSize": 1,
            "current": 1
        }
        data = {
            'list': devices,
            'pagination': pagination
        }


        return data, True