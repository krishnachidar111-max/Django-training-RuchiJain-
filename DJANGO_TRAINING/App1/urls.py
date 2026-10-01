from django.urls import path
from App1 import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.hello, name="hello"),
    path("about/", views.about, name="about"),
]
