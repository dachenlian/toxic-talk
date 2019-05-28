from itertools import zip_longest

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
        ).json()
        comments = r.get('comments')
        sampled = r.get('sampled')
        combined = list(zip_longest(comments, sampled, fillvalue=""))
        context = {
            'combined': combined,
            'intext': text,
        }
        return render(request, self.template_name, context=context)
