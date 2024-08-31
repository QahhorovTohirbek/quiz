from . import serializers
from main import models

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def quiz_detail(request, code):
    quiz = models.Quiz.objects.get(code=code)
    quiz_serializer = serializers.QuizSerializer(quiz)
    question = models.Question.objects.filter(quiz=quiz)
    question_serializer = serializers.QuestionSerializer(question)

    return Response(
        {
            'quiz':quiz_serializer.data,
            'question':question_serializer.data,
        }
    )



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def answer_create(request, code):
    quiz = models.Quiz.objects.get(code, code)
    user_name = request.data.get('user_name')
    phone = request.data.get('phone')
    email = request.data.get('email')
    answers = models.Answer.objects.create(
        quiz = quiz,
        user_name = user_name,
        phone = phone,
        email = email, 
    )

    answers = request.data.get('answers')
    correct = 0 
    wrong = 0
    for key, value in answers.items():
        question = models.Question.objects.get(code=key)
        option = models.Option.objects.get(code=value)
        answer_detail = models.AnswerDetail.objects.create(
            answers = answers,
            question = question,
            user_answer = option,
        )
        if answer_detail.is_correct:
            correct+=1
    
    total = models.Question.objects.filter(quiz=quiz).count()
    wrong = total - correct
    correct_persentage = int(correct*100/total)
    wrong_persentage = 100 - correct_persentage

    return Response({

        'status':True,
        'total':total,
        'correct':correct,
        "wrong":wrong,
        'correct_persentage':correct_persentage,
        'wrong_persentage':wrong_persentage
        
    })



@api_view(['POST'])
def log_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token':token.key})
    return Response



@api_view(['POST'])
def log_out(request):
    token = Token.objects.get(user = request.user).delete()
    return Response













