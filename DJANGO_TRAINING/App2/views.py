from django.http import HttpResponse

def index(request):
    return HttpResponse("This is App2")

def facebook(request):
    return HttpResponse("Welcome to App2 - Facebook Page")

def linkedIn(request):
    return HttpResponse("Welcome to App2 - LinkedIn Page")
