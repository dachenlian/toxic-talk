from django.shortcuts import render
from django.views.generic import View

import requests


class IndexView(View):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        text = request.POST.get('seed')
        data = {
            'seed': text,
        }
        r = request.post(
            'url',
            data=data,
        )
        context = {
            'result': r,
        }
        return render(request, self.template_name, context=context)
