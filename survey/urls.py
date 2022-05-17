from unicodedata import name
from django.urls import path
from survey import views

app_name = 'survey'

urlpatterns = [
    path('survey-start/', views.question0, name='survey_q0'),
    path('survey-q1/', views.question1, name='survey_q1'),
    path('survey-q2/', views.question2, name='survey_q2'),
    path('survey-q3/', views.question3, name='survey_q3'),
    path('survey-q4/', views.question4, name='survey_q4'),
    path('survey-q5/', views.question5, name='survey_q5'),
    path('survey-q6/', views.question6, name='survey_q6'),
    path('survey-q7/', views.question7, name='survey_q7'),
    path('survey-q8/', views.question8, name='survey_q8'),
    path('survey-q9/', views.question9, name='survey_q9'),
    path('survey-q10/', views.question10, name='survey_q10'),
    path('survey-end/', views.survey_end, name='survey_end'),
]