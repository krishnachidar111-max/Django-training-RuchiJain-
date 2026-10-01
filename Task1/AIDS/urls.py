from django.urls import path
from . import views

urlpatterns = [
    path('', views.About_AIDS, name='about_aids'),
]
