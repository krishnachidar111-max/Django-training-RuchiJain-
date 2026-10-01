from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),

    path('home/', views.home, name='home'),

    path('signup/', views.signup, name='signup'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('quiz/<int:quiz_id>/', views.start_quiz, name='start_quiz'),

    path('history/', views.history, name='history'),

    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),

    path('admin-panel/add-quiz/', views.add_quiz, name='add_quiz'),

    path('admin-panel/quiz/delete/<int:quiz_id>/', views.delete_quiz, name='delete_quiz'),

    path('admin-panel/add-question/', views.add_question, name='add_question'),

    path('admin-panel/questions/', views.manage_questions, name='manage_questions'),

    path('admin-panel/questions/edit/<int:question_id>/', views.edit_question, name='edit_question'),

    path('admin-panel/questions/delete/<int:question_id>/', views.delete_question, name='delete_question'),

    path('admin-panel/results/', views.view_results, name='view_results'),
]
