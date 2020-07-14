from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *

class question_list(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        question_list = Question.objects.filter(posted_by = request.user).values('id','question_text','date')
        return Response({"question_list":question_list})


class answer_list(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        answer_list = Answer.objects.filter(answered_by = request.user).values('id','answer_text','date')
        return Response({"answer_list":answer_list})


class upvote_list(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        upvote_list = Upvote.objects.filter(upvoted_by = request.user).values('id','answer__answer_text','date')
        return Response({"upvote_list":upvote_list})


class question_answer_list(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, question_id):
        question = Question.objects.get(id = question_id)
        answer_list = Answer.objects.filter(question = question).values('answer_text')
        return Response({"question":question.question_text,"answer_list":answer_list})

class answer_upvoted_list(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, answer_id):
        answer = Answer.objects.get(id = answer_id)
        upvoted_list = Upvote.objects.filter(answer = answer).values('upvoted_by__username')
        return Response({"question":answer.question.question_text,"answer":answer.answer_text,"upvoted_by":upvoted_list})


from django.db.models import Count
from django.db.models import Max
from django.utils import timezone

class highest_up_voted_question_past_hour(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        #upvote = Upvote.objects.values('answer__question__question_text').order_by().annotate(upvote_count=Count('answer__question__question_text')).aggregate(maxval=Max('upvote_count'))
        upvote = Upvote.objects.filter(date__gt = timezone.now()-timezone.timedelta(hours=1)).values('answer__question__question_text').order_by().annotate(upvote_count=Count('answer__question__question_text'))
        question = ''
        max_upvote = 0
        for item in upvote:
            if item['upvote_count'] > max_upvote:
                max_upvote = item['upvote_count']
                question = item['answer__question__question_text']
        return Response({"question":question,"max_upvote":max_upvote})

class highest_up_voted_question(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        #upvote = Upvote.objects.values('answer__question__question_text').order_by().annotate(upvote_count=Count('answer__question__question_text')).aggregate(maxval=Max('upvote_count'))
        upvote = Upvote.objects.values('answer__question__question_text').order_by().annotate(upvote_count=Count('answer__question__question_text'))
        question = ''
        max_upvote = 0
        for item in upvote:
            if item['upvote_count'] > max_upvote:
                max_upvote = item['upvote_count']
                question = item['answer__question__question_text']
        return Response({"question":question,"max_upvote":max_upvote})