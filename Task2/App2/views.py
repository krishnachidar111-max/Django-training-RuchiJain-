from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def sistec(request):
    template = loader.get_template('sistec.html')
    res = template.render()
    return HttpResponse(res)
