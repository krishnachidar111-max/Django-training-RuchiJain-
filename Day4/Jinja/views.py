from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def info(request):
    name="KRISHNA CHIDAR"
    section="AIDS"
    college="SISTEC"
    context={
        "name":name,
        "section":section,
        "college":college,
    }   
    template=loader.get_template("info.html")
    res=template.render(context,request)
    return HttpResponse(res)    


def testpaper(request):
    que="who develope python"
    a="James Gosling"
    b="Bjarne Stroustrup"
    c="Guido Van Rossum"
    d="Tim Berners-Lee"
    context={
        "que":que,
        "a":a,
        "b":b,
        "c":c,
        "d":d,
    }   
    template=loader.get_template("testpaper.html")
    res=template.render(context,request)
    return HttpResponse(res)


def sum(request):
    a=10
    b=20
    c=20
    d=a+b+c
    context={
        'a':a,
        'b':b,
        'c':c,
        'd':d
    }
    template=loader.get_template('sum.html')
    res=template.render(context,request)
    return HttpResponse(res)



def result(request):
    context={
        "name":"Krishna chidar",
        "marks":98,
        "section":"AIDS",
        "college":"SISTEC",
    }
    return render(request,"result.html",context)

def voting(request):
    context={
        "name":"Krishna Chidar",
        "age":20, 
    }
    return render(request,"voting.html",context)

def shopping(request):
    return render(request, "shopping.html")