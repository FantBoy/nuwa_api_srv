#_*_ coding: utf-8 _*_
from __future__ import unicode_literals
from common.ErrorModule.ErrorBase import ErrorClass
import logging
logger = logging.getLogger('django')

class AbcmouseWeChatServerException(Exception):
    def __init__(self, error_class, except_msg):
        if isinstance(error_class, ErrorClass):
            self.message = error_class.ERROR_MSG
            self.status = error_class.ERROR_CODE
            self.except_msg = except_msg
            self.response_msg = error_class.ERROR_RESPONSE_MSG
            self.log()
        else:
            logger.error("error_class is not exist in ErrorClass")

    def log(self):
        error_str = """[ret] {error_code}({error_msg}), [except_msg] {except_msg}""".format(
            error_code = self.status,
            error_msg = self.message,
            except_msg = self.except_msg
        )
        logger.error(error_str)

    def __str__(self):
        error_str = """[ret] {error_code}({error_msg}), [except_msg] {except_msg}""".format(
            error_code = self.status,
            error_msg = self.message,
            except_msg = self.except_msg
        )
        return error_str

    def responseMsg(self):
        return self.response_msg
