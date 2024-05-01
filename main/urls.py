from django.urls import path
from . import views

urlpatterns = [
    path('quiz-create', views.quiz_create)
]