from django.shortcuts import render, redirect
from main import models
from django.contrib.auth.models import User


def index(request):
    quizzes = models.Quiz.objects.filter(author=request.user)
    users = models.User.objects.all().count()
    quiz = models.Quiz.objects.all()
    questions = models.Question.objects.all()
    context = {
        'users':users,
        'quizzes':quizzes,
        'quiz':quiz,
        'questions':questions,
    }

    return render(request, 'index.html', context)


def quiz_create(request):
    if request.method == 'POST':
        name = request.POST.get('name') 
        if request.user.is_authenticated:
            quiz = models.Quiz.objects.create(name=name, author=request.user)
            return redirect('quiz_detail', code=quiz.code)
        else:
            return redirect('login')
    return render(request, 'quiz-create.html')


def quiz_detail(request, code):
    quiz = models.Quiz.objects.get(code=code)
    questions = models.Question.objects.filter(quiz=quiz)
    context = {
        'quiz':quiz,
        'questions':questions
    }
    return render(request, 'quiz-detail.html', context)


def question_create(request, code):
    quiz = models.Quiz.objects.get(code=code)
    question = models.Question.objects.create(
        name=request.POST['name'],
        quiz=quiz
        )
    models.Option.objects.create(
        name = request.POST['correct_option'],
        question = question,
        is_correct = True
    )
    for option in request.POST.list('options'):
        models.Option.objects.create(
        name = option,
        question = question,
        is_correct = False
        )
    return redirect('quiz_detail', quiz.code)


def question_detail(request, code):
    question = models.Question.objects.get(code=code)
    return render(request, 'question-detail.html', {'question':question})