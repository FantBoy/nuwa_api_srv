#_*_ coding: utf-8 _*_
from __future__ import unicode_literals

class ErrorClass(object):
    def __init__(self, error_code, error_msg):
        self.error_code = error_code
        self.error_msg = error_msg
    @property
    def ERROR_CODE(self):
        return self.error_code
    @property
    def ERROR_MSG(self):
        return self.error_msg
    @property
    def ERROR_RESPONSE_MSG(self):
        result = {'ret': self.error_code, 'msg': self.error_msg}
        return result
