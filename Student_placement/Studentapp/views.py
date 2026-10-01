import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from Studentapp.models import Student
import joblib

# Resolve model paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCALER_PATH = os.path.join(BASE_DIR, 'scalermodel.pkl')
MODEL_PATH = os.path.join(BASE_DIR, 'mlmodel.pkl')

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def save_student(request):
    if request.method == 'POST':
        s_id = request.POST.get('S_Id') or request.POST.get('Student_Id')
        s_name = request.POST.get('S_Name') or request.POST.get('Student_Name')
        s_pass = request.POST.get('S_Pass') or request.POST.get('password')
        s_email = request.POST.get('S_Email') or request.POST.get('Student_Email')
        s_no = request.POST.get('S_No') or request.POST.get('Student_No', '')

        if not s_id or not s_name:
            return render(request, 'register.html', {'error': 'Student ID and Name are required!'})

        already_exists = Student.objects.filter(S_Id=s_id).exists()
        if already_exists:
            return render(request, 'register.html', {'error': 'Student with this ID already exists!'})

        student = Student(
            S_Id=s_id,
            S_Name=s_name,
            S_Pass=s_pass,
            S_Email=s_email,
            S_No=s_no
        )
        student.save()
        return HttpResponseRedirect(reverse('login'))
    return HttpResponseRedirect(reverse('register'))

def login(request):
    return render(request, 'login.html')

def login_validation(request):
    if request.method == 'POST':
        s_name = request.POST.get('S_Name') or request.POST.get('username')
        s_pass = request.POST.get('S_Pass') or request.POST.get('password')

        student = Student.objects.filter(S_Pass=s_pass).filter(Q(S_Name=s_name) | Q(S_Id=s_name)).first()
        if student:
            request.session['student_name'] = student.S_Name
            request.session['student_id'] = student.S_Id
            return HttpResponseRedirect(reverse('predict'))
        else:
            return render(request, 'login.html', {'error': 'Invalid Username/ID or Password!'})
    return HttpResponseRedirect(reverse('login'))

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('home'))

def predict(request):
    student_name = request.session.get('student_name', '')
    return render(request, 'predict.html', {'student_name': student_name})

def result(request):
    scaler = joblib.load(SCALER_PATH)
    mlmodel = joblib.load(MODEL_PATH)

    cgpa = float(request.GET.get('cgpa', 0))
    iq = float(request.GET.get('iq', 0))
    profile_score = float(request.GET.get('profile_score', 0))

    list_vals = [cgpa, iq, profile_score]
    scaled_input = scaler.transform([list_vals])
    ans = int(mlmodel.predict(scaled_input)[0])

    student_name = request.session.get('student_name', '')

    context = {
        'ans': ans,
        'list': list_vals,
        'cgpa': cgpa,
        'iq': iq,
        'profile_score': profile_score,
        'student_name': student_name
    }
    return render(request, 'result.html', context)
