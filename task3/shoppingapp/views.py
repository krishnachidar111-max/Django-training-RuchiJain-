from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
 

def shoppingapp(request):
    return render(request,'shopping.html')

    
