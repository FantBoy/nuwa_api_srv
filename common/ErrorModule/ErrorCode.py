#_*_ coding: utf-8 _*_
from __future__ import unicode_literals

from common.ErrorModule.ErrorBase import ErrorClass

OK = ErrorClass(0, '正常')
PostParamsError = ErrorClass(-1001, '参数异常')
