from django.forms import ModelForm
from . import models


class QuizForm(ModelForm):
    class Meta:
        model = models.Quiz
        fields = '__all__'


class QuestionForm(ModelForm):
    class Meta:
        model = models.Question
        fields = ['name']