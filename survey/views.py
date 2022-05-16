from django.db.utils import OperationalError
from django.shortcuts import redirect, render
from survey.models import SurveyQuestion

import uuid

# Create your views here.

def question0(request):
    if request.method == "POST":
        activity_answer = SurveyQuestion()
        activity_answer.survey_uid = request.COOKIES.get("supme-survey-id")
        activity_answer.question0 = request.POST.get('start')
        activity_answer.save()
        return redirect("survey:survey_q1")
    response = render(request, 'survey/survey_q0.html')
    response.set_cookie("supme-survey-id", str(uuid.uuid4()))
    return response

# def question1(request):
#     if request.method == "POST":
#         activity_answer = SurveyQuestion()
#         activity_answer.survey_uid = request.COOKIES.get("supme-survey-id")
#         activity_answer.question1 = request.POST.get('where')
#         activity_answer.save()
#         return redirect("survey:survey_q2")
#     response = render(request, 'survey/survey_q1.html')
#     response.set_cookie("supme-survey-id", str(uuid.uuid4()))
#     return response

def question1(request):
    survey_uid = request.COOKIES.get("supme-survey-id")
    if not survey_uid:
        return redirect("mypage:home")
    if request.method == "POST":
        try:
            activity_answer = SurveyQuestion.objects.get(survey_uid=survey_uid)
        except OperationalError:
            return redirect("mypage:home")
        activity_answer.question1 = request.POST.get('where')
        activity_answer.save()
        return redirect("survey:survey_q2")
    return render(request, 'survey/survey_q1.html')

def question2(request):
    survey_uid = request.COOKIES.get("supme-survey-id")
    if not survey_uid:
        return redirect("mypage:home")
    if request.method == "POST":
        try:
            activity_answer = SurveyQuestion.objects.get(survey_uid=survey_uid)
        except OperationalError:
            return redirect("mypage:home")
        activity_answer.question2 = request.POST.get('gender')
        activity_answer.save()
        return redirect("survey:survey_q3")
    return render(request, 'survey/survey_q2.html')


def question3(request):
    survey_uid = request.COOKIES.get("supme-survey-id")
    if not survey_uid:
        return redirect("mypage:home")
    if request.method == "POST":
        try:
            activity_answer = SurveyQuestion.objects.get(survey_uid=survey_uid)
        except OperationalError:
            return redirect("mypage:home")
        activity_answer.question3 = request.POST.get('where')
        activity_answer.save()
        return redirect("survey:survey_q4")
    return render(request, 'survey/survey_q3.html')

def question4(request):
    survey_uid = request.COOKIES.get("supme-survey-id")
    if not survey_uid:
        return redirect("mypage:home")
    if request.method == "POST":
        try:
            activity_answer = SurveyQuestion.objects.get(survey_uid=survey_uid)
        except OperationalError:
            return redirect("mypage:home")
        activity_answer.question4 = request.POST.get('where')
        activity_answer.save()
        return redirect("survey:survey_q5")
    return render(request, 'survey/survey_q4.html')

def question5(request):
    survey_uid = request.COOKIES.get("supme-survey-id")
    if not survey_uid:
        return redirect("mypage:home")
    if request.method == "POST":
        try:
            activity_answer = SurveyQuestion.objects.get(survey_uid=survey_uid)
        except OperationalError:
            return redirect("mypage:home")
        activity_answer.question5 = request.POST.get('where')
        activity_answer.save()
        return redirect("survey:survey_q6")
    return render(request, 'survey/survey_q5.html')

def question6(request):
    survey_uid = request.COOKIES.get("supme-survey-id")
    if not survey_uid:
        return redirect("mypage:home")
    if request.method == "POST":
        try:
            activity_answer = SurveyQuestion.objects.get(survey_uid=survey_uid)
        except OperationalError:
            return redirect("mypage:home")
        activity_answer.question6 = request.POST.get('where')
        activity_answer.save()
        return redirect("survey:survey_q7")
    return render(request, 'survey/survey_q6.html')

def question7(request):
    survey_uid = request.COOKIES.get("supme-survey-id")
    if not survey_uid:
        return redirect("mypage:home")
    if request.method == "POST":
        try:
            activity_answer = SurveyQuestion.objects.get(survey_uid=survey_uid)
        except OperationalError:
            return redirect("mypage:home")
        activity_answer.question7 = request.POST.get('where')
        activity_answer.save()
        return redirect("survey:survey_q8")
    return render(request, 'survey/survey_q7.html')

def question8(request):
    survey_uid = request.COOKIES.get("supme-survey-id")
    if not survey_uid:
        return redirect("mypage:home")
    if request.method == "POST":
        try:
            activity_answer = SurveyQuestion.objects.get(survey_uid=survey_uid)
        except OperationalError:
            return redirect("mypage:home")
        activity_answer.question8 = request.POST.get('where')
        activity_answer.save()
        return redirect("survey:survey_q9")
    return render(request, 'survey/survey_q8.html')

def question9(request):
    survey_uid = request.COOKIES.get("supme-survey-id")
    if not survey_uid:
        return redirect("mypage:home")
    if request.method == "POST":
        try:
            activity_answer = SurveyQuestion.objects.get(survey_uid=survey_uid)
        except OperationalError:
            return redirect("mypage:home")
        activity_answer.question9 = request.POST.get('where')
        activity_answer.save()
        return redirect("survey:survey_end")
    return render(request, 'survey/survey_q9.html')

def survey_end(request):
    survey_uid = request.COOKIES.get("supme-survey-id")
    if not survey_uid:
        return redirect("mypage:home")
    if request.method == "POST":
        try:
            activity_answer = SurveyQuestion.objects.get(survey_uid=survey_uid)
        except OperationalError:
            return redirect("mypage:home")
        activity_answer.question10 = request.POST.get('where')
        activity_answer.save()
        return redirect("mypage:login")
    return render(request, 'survey/survey_q10.html')