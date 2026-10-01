from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from myuser.models import user
from django.urls import reverse



def home(request):
    return render(request,'home.html')
def signup(request):
    return render(request,'signup.html')
def saveuser(request):
    username = request.POST['username']
    already_exists = user.objects.filter(username=username).exists()
    if not already_exists:
        u = user()
        u.username = username
        u.password = request.POST['password']
        u.name = request.POST['name']
        u.save()
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'signup.html', {'error': 'user already exists'})
def login(request):
    return render(request,'login.html')

def loginvalidation(request):
    try:
        user1 = user.objects.get(username = request.POST['username'],password = request.POST['password'])
         #---------------------session create-------------------------------------#
        request.session['username'] =user1.username
        request.session['name'] =user1.name
        return HttpResponseRedirect(reverse('home'))
    except user.DoesNotExist:
        return render(request,'login.html',{'error':'invalid username or password'})
def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('login'))
    
