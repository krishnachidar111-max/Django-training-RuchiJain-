from django.contrib import admin
from django.urls import path
from Studentapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('save_student/', views.save_student, name='save_student'),
    path('login/', views.login, name='login'),
    path('login_validation/', views.login_validation, name='login_validation'),
    path('predict/', views.predict, name='predict'),
    path('result/', views.result, name='result'),
    path('logout/', views.logout, name='logout'),
    path('admin/', admin.site.urls),
]
