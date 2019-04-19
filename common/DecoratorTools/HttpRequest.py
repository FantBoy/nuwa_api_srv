# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
-------------------------------------------------
   File Name：     HttpRequest
   Description :   http请求装饰器，请求耗时统计和关键日志输出
   Author :       bearboyxu
   date：          2018/1/29
-------------------------------------------------
   Change Activity:
                   2018/1/29:
-------------------------------------------------
"""
__author__ = 'bearboyxu'

import logging
from django.http import HttpResponse, JsonResponse
import json
import time
import socket, fcntl, struct

logger = logging.getLogger('collect')

def get_ipaddress():
  try:
      ifname = 'eth1'
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
      ip = socket.inet_ntoa(inet[20:24])
      return ip
  except:
    return "127.0.0.1"

def encode_dc_log(dclog):
    keyvalues = []
    for key, value in dclog.iteritems():
        keyvalues.append("""{}={}""".format(key, value))
    return '&'.join(keyvalues)

def HttpRequestDecorator(func):

    def wrapper(*args, **kw):
        t1 = time.time()
        log = """START\n\n{step}{useragent}\n{step}{forwordip}\n{step}{path}\n{step}{classname}\n{step}{funcname}\n{step}{getdata}\n{step}{postdata}\n""".format(
            useragent = args[1].META.get('HTTP_USER_AGENT', ''),
            forwordip = args[1].META.get('HTTP_X_FORWARDED_FOR', ''),
            path = args[1].path,
            classname = args[0].__class__,
            funcname = func.__name__,
            getdata = args[1].GET,
            postdata = args[1].POST,
            step='                          '

        )

        logger.debug(log)
        res_data = func(*args, **kw)
        t2 = time.time()
        logger.debug("""ret: {}, timecust: {}""".format(res_data.get('ret', None), t2 - t1))
        # response = HttpResponse(content_type='application/json')
        # json.dump(res_data, response)
        logger.debug('END')

        return JsonResponse(res_data)
    return wrapper
