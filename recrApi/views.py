# -*- coding: utf-8 -*-

import re

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class BasicView(View):
    def get(self, request, name, message, *args, **kwargs):
        return HttpResponse(f"Hello, {name}! {message}!", charset="UTF-8")


class AnchoredView(View):
    def get(self, request, *args, **kwargs):
        data = request.get_full_path()
        regexp = re.compile(r'^/\?name=(.*)&message=(.*)')
        if regexp.search(data):
            name_and_message = re.search('^/\?name=(.*)&message=(.*)', data)
            if name_and_message:
                name = name_and_message.group(1)
                message = name_and_message.group(2)
            return HttpResponse(f"Hello, {name}! {message}!", charset="UTF-8")

        return HttpResponse(f"nope")
