from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-up/save/', views.save_user, name='save_user'),
    path('login/', views.login, name='login'),
    path('login/validate/', views.login_vel, name='login_vel'),
    path('students/register/', views.student_registration, name='student_registration'),
    path('logout/', views.logout_view, name='logout'),
]
