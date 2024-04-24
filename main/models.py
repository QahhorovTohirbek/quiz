from django.db import models
from django.contrib.auth.models import User

from random import sample
import string


class CodeGenerator(models.Model):
    code = models.CharField(max_length=255, null=True, blank=True)

    @staticmethod
    def generatecode():
        return ''.join(sample(string.ascii_letters + string.digits, 15))
    
    def save(self, *args, **kwargs):
        if not self.pk:
            while  True:
                code = self.generatecode()
                if not self.__class__.objects.filter(code=code).exists():
                    self.code = code
                    break
        super().save(*args, **kwargs)
    
    class Meta:
        abstract = True



class Quiz(CodeGenerator):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)



    def __str__(self) -> str:
        return self.name
    

class Question(CodeGenerator):
    name = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    @property
    def correct_answer(self):
        return Option.objects.get(question=self, is_correct=True)
    
    @property
    def options(self):
        return Option.objects.fil(question=self)





class Option(CodeGenerator):
    name = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        options = Option.objects.filter(question = self.question).count()
        first = options==0
        correct = self.is_correct
        if (first and correct) or (not first and not correct):
            super(Option, self).save(*args, **kwargs)
        else:
            raise ValueError
    

class Answer(models.Model):
    user_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class AnswerDetail(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question ,on_delete=models.CASCADE)
    user_answer = models.ForeignKey(Option, on_delete=models.CASCADE)


    @property
    def is_correct(self):
        return self.user_answer == self.question.correct_answer