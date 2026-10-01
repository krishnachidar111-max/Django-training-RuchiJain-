from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from .models import Quiz, TestResult, Question

# Landing Page: This is the first page of our website
def landing(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'landing.html')


# Home Page: Shows a list of quizzes. User must be logged in.
@login_required
def home(request):
    quizzes = Quiz.objects.all().order_by('id')
    return render(request, 'home.html', {'quizzes': quizzes})


# Logout View: Handles both GET and POST requests safely without 405 errors
def logout_view(request):
    auth_logout(request)
    return redirect('landing')


# Signup Page: Allows new users to create an account
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Automatically log the user in after signing up
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# Start Quiz: Where the user answers questions and gets a score
@login_required
def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all().order_by('id')[:quiz.number_of_questions]
    total_q = questions.count()
    
    if request.method == 'POST':
        score = 0
        # Check every question to see if the chosen answer is correct
        for question in questions:
            selected_answer = request.POST.get(f'question_{question.id}')
            if selected_answer and selected_answer.strip() == question.correct_answer.strip():
                score += 1
                
        # Save the final score into our database
        TestResult.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total_questions=total_q
        )
        percentage = round((score / total_q) * 100) if total_q > 0 else 0
        return render(request, 'result.html', {
            'quiz': quiz,
            'score': score,
            'total': total_q,
            'percentage': percentage
        })

    # Show the quiz page with all questions
    return render(request, 'quiz.html', {
        'quiz': quiz,
        'questions': questions,
        'total_questions': total_q
    })


# History: Shows past test results for the current user
@login_required
def history(request):
    # Fetch results for the logged-in user, ordered by newest first
    results = TestResult.objects.filter(user=request.user).order_by('-attempted_at')
    total_attempts = results.count()
    best_score = max([r.score for r in results], default=0) if total_attempts > 0 else 0
    return render(request, 'history.html', {
        'results': results,
        'total_attempts': total_attempts,
        'best_score': best_score
    })


# Admin Dashboard: Main control panel for the site admin
def admin_dashboard(request):
    quizzes = Quiz.objects.all().order_by('-id')
    total_quizzes = quizzes.count()
    total_questions = Question.objects.count()
    total_results = TestResult.objects.count()
    return render(request, 'admin_dashboard.html', {
        'quizzes': quizzes,
        'total_quizzes': total_quizzes,
        'total_questions': total_questions,
        'total_results': total_results
    })


# Add Quiz: Create a new quiz topic
def add_quiz(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number_of_questions = request.POST.get('number_of_questions')
        if name and number_of_questions:
            Quiz.objects.create(name=name.strip(), number_of_questions=int(number_of_questions))
            return redirect('admin_dashboard')
        
    return render(request, 'add_quiz.html')


# Delete Quiz: Remove a quiz
def delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.delete()
    return redirect('admin_dashboard')


# Add Question: Create a new question and assign it to a quiz
def add_question(request):
    quizzes = Quiz.objects.all().order_by('name')
    
    if request.method == 'POST':
        quiz_id = request.POST.get('quiz')
        if quiz_id:
            quiz = get_object_or_404(Quiz, id=quiz_id)
            Question.objects.create(
                quiz=quiz,
                question_text=request.POST.get('question_text', '').strip(),
                option1=request.POST.get('option1', '').strip(),
                option2=request.POST.get('option2', '').strip(),
                option3=request.POST.get('option3', '').strip(),
                option4=request.POST.get('option4', '').strip(),
                correct_answer=request.POST.get('correct_answer', '').strip()
            )
            return redirect('manage_questions')
        
    return render(request, 'add_question.html', {'quizzes': quizzes})


# Manage Questions: View all questions in the database
def manage_questions(request):
    questions = Question.objects.all().select_related('quiz').order_by('-id')
    return render(request, 'manage_questions.html', {'questions': questions})


# Edit Question: Update details of an existing question
def edit_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    quizzes = Quiz.objects.all().order_by('name')
    
    if request.method == 'POST':
        quiz_id = request.POST.get('quiz')
        if quiz_id:
            question.quiz = get_object_or_404(Quiz, id=quiz_id)
        question.question_text = request.POST.get('question_text', '').strip()
        question.option1 = request.POST.get('option1', '').strip()
        question.option2 = request.POST.get('option2', '').strip()
        question.option3 = request.POST.get('option3', '').strip()
        question.option4 = request.POST.get('option4', '').strip()
        question.correct_answer = request.POST.get('correct_answer', '').strip()
        
        question.save()
        return redirect('manage_questions')
        
    return render(request, 'edit_question.html', {'question': question, 'quizzes': quizzes})


# Delete Question: Remove a question entirely
def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.delete()
    return redirect('manage_questions')


# View Results: Admin view to see scores of all students
def view_results(request):
    results = TestResult.objects.all().select_related('user', 'quiz').order_by('-attempted_at')
    return render(request, 'view_results.html', {'results': results})