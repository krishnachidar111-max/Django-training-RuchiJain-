from django.http import HttpResponse

def index(request):
    return HttpResponse("This is App1")

def hello(request):
    return HttpResponse("Hello from App1!")

def about(request):
    return HttpResponse("About App1")
