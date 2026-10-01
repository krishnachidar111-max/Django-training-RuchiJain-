from django.urls import path
from App2 import views

urlpatterns = [
    path("facebook/", views.facebook),
    path("linkdin/", views.linkedIn),
]
