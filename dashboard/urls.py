from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    # quiz 
    path('quiz-create/', views.quiz_create, name='quiz_create'),
    path('quiz-detail/', views.quiz_detail, name='quiz_detail'),
    path('quiz-list/', views.quiz_list, name='quiz_list'),
    path('quiz-update/<str:code>/', views.quiz_update, name='quiz_update'),
    path('quiz-detail/<str:code>/', views.quiz_detail, name='quiz_detail'),
    path('quiz-delete/<str:code>/', views.quiz_delete, name='quiz_delete'),
    # question
    path('question-create/<str:code>/', views.question_create, name='question_create'),
    path('question-detail/<str:code>/', views.question_detail, name='question_detail'),
    path('question-update/<str:code>/', views.question_update, name='question_update'),
    path('question-delete/<str:code>/', views.question_delete, name='question_delete'),
    # answer
    path('answer-list/<str:code>/', views.answer_list, name='answer_list'),
    path('answer-detail/<str:code>/', views.answer_detail, name='answer_detail'),
    path('write-excel/<str:code>/', views.write_excel, name='write_excel'),
    

    # user
    path('log-in/', views.log_in, name='log_in'),
    path('log-out/', views.log_out, name='log_out'),
]
