import re

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def test(request):
    return HttpResponse('id:')


# Create your views here.
class BasicView(View):
    def get(self, request, name, message, *args, **kwargs):
        print(request)
        print(request.get_full_path())
        return HttpResponse(f"Basic View:\nHello, {name}! {message}!", content_type="text/plain")


class AnchoredView(View):
    def get(self, request, *args, **kwargs):
        data = request.get_full_path()
        print(data)
        regexp = re.compile(r'^/\?name=(.*)&message=(.*)')
        if regexp.search(data):
            name_and_message = re.search('^/\?name=(.*)&message=(.*)', data)
            if name_and_message:
                name = name_and_message.group(1)
                message = name_and_message.group(2)
            return HttpResponse(f"Hello, {name}! {message}!")

        return HttpResponse(f"nope")
