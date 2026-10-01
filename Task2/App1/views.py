from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def quiz(request):
    template = loader.get_template('quiz.html')
    res = template.render({}, request)
    return HttpResponse(res)
