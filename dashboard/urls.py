from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz-create/', views.quiz_create, name='quiz_create'),
    path('quiz-detail/', views.quiz_detail, name='quiz_detail'),
    path('quiz-detail/<str:code>/', views.quiz_detail, name='quiz_detail'),
    path('question-create/<str:code>/', views.question_create, name='question_create'),
    path('question-detail/<str:code>/', views.question_detail, name='question_detail'),
]
