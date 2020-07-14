from django.urls import path, include
from .views import *

urlpatterns = [
    path('question_list/',question_list.as_view(),name='user-question-list'),
    path('answer_list/',answer_list.as_view(),name='user-answer-list'),
    path('upvote_list/',upvote_list.as_view(),name='user-upvote-list'),
    path('question/<question_id>/answer_list/',question_answer_list.as_view(),name='question-answer-list'),
    path('answer/<answer_id>/upvoted_list/',answer_upvoted_list.as_view(),name='answer-upvoted-list'),
    path('question/highest_upvote/last_hour/',highest_up_voted_question_past_hour.as_view(),name='highest-up-voted-question-hour'),
    path('question/highest_upvote/',highest_up_voted_question.as_view(),name='highest-up-voted-question'),
]
