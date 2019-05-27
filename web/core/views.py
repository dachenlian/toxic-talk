from django.shortcuts import render
from django.views.generic import View

import requests


class IndexView(View):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        text = request.POST.get('intext')
        data = {
            'intext': text,
        }
        r = requests.post(
            'http://140.112.147.120:15000/textgen',
            json=data,
        ).json().get('comments')
        context = {
            'comments': r,
            'intext': text,
        }
        return render(request, self.template_name, context=context)
