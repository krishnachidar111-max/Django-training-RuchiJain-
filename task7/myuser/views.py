from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import redirect, render
from .models import PortalUser,StudentRegistration

SESSION_USER_ID = 'task7_portal_user_id'


def _current_user(request):
    user_id = request.session.get(SESSION_USER_ID)
    if user_id is None:
        return None
    return PortalUser.objects.filter(pk=user_id).first()


def home(request):
    return render(request, 'home.html', {'portal_user': _current_user(request)})


def sign_up(request):
    return render(request, 'sign_up.html')


def save_user(request):
    if request.method != 'POST':
        return redirect('sign_up')

    username = request.POST.get('username', '').strip()
    name = request.POST.get('name', '').strip()
    password = request.POST.get('password', '')

    if not username or not name or not password:
        return render(request, 'sign_up.html', {
            'errormsg': 'Please fill in all fields.'
        })
    if PortalUser.objects.filter(username=username).exists():
        return render(request, 'sign_up.html', {
            'errormsg': 'That username is already in use.'
        })

    PortalUser.objects.create(
        username=username,
        name=name,
        password=make_password(password),
    )
    return redirect('login')


def login(request):
    return render(request, 'login.html')


def login_vel(request):
    if request.method != 'POST':
        return redirect('login')

    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '')
    portal_user = PortalUser.objects.filter(username=username).first()

    if portal_user is None or not check_password(password, portal_user.password):
        return render(request, 'login.html', {
            'errormsg': 'Incorrect username or password.'
        })

    request.session[SESSION_USER_ID] = portal_user.pk
    return redirect('student_registration')


def student_registration(request):
    portal_user = _current_user(request)
    if portal_user is None:
        return redirect('login')

    if request.method == 'POST':
        student_id = request.POST.get('student_id', '').strip()
        student_name = request.POST.get('student_name', '').strip()
        semester = request.POST.get('semester', '').strip()
        subject = request.POST.get('subject', '').strip()

        if not all((student_id, student_name, semester, subject)):
            students = StudentRegistration.objects.filter(
                registered_by=portal_user
            ).order_by('student_name')
            return render(request, 'student_registration.html', {
                'portal_user': portal_user,
                'students': students,
                'errormsg': 'Please fill in all fields.',
            })

        if StudentRegistration.objects.filter(student_id=student_id).exists():
            students = StudentRegistration.objects.filter(
                registered_by=portal_user
            ).order_by('student_name')
            return render(request, 'student_registration.html', {
                'portal_user': portal_user,
                'students': students,
                'errormsg': 'That student ID is already registered.',
            })

        StudentRegistration.objects.create(
            student_id=student_id,
            student_name=student_name,
            semester=semester,
            subject=subject,
            registered_by=portal_user,
        )
        request.session['task7_registration_saved'] = True
        return redirect('student_registration')

    students = StudentRegistration.objects.filter(
        registered_by=portal_user
    ).order_by('student_name')
    saved = request.session.pop('task7_registration_saved', False)
    return render(request, 'student_registration.html', {
        'portal_user': portal_user,
        'students': students,
        'saved': saved,
    })


def logout_view(request):
    request.session.flush()
    return redirect('home')
