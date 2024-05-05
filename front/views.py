from django.shortcuts import render, redirect
from main import models
import random


def index(request):
    quizzes = models.Quiz.objects.all()
    context = {
        'quizzes':quizzes
    }
    return render(request, 'front/index.html', context)



def quiz_detail(request, code):
  quiz = models.Quiz.objects.get(code=code)
  questions = models.Question.objects.filter(quiz=quiz)
  questions_list = list(questions)
  random.shuffle(questions_list)
  
  context = {
    'quiz': quiz,
    'questions': questions_list
    }
  if request.method == 'POST':
    answer = models.Answer.objects.create(
        quiz=quiz,
        user_name=request.POST.get('user_name'),
        phone=request.POST.get('phone'),
        email=request.POST.get('email')
    )
    for key, value in request.POST.items():
      if key.startswith('question'):
        question_id = int(key[len('question['):-len(']')])
       
        models.AnswerDetail.objects.create(
            answer=answer,
            question_id=question_id,
            user_answer_id=int(value)
        )
  
  return render(request, 'front/quiz-detail.html', context)
