from django.urls import path
from . import views

urlpatterns = [
    path('', views.About_about, name='about_about'),
]
