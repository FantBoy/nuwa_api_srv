from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

import logging 
logger = logging.getLogger('django')


class Add(View):
    def get(self, request):
        return HttpResponse("sssssss") 