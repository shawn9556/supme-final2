from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SurveyQuestion(models.Model):
    survey_uid = models.CharField(max_length=64)
    question0 = models.CharField(max_length=32, null=True, blank=True)
    question1 = models.CharField(max_length=32, null=True, blank=True)
    question2 = models.CharField(max_length=32, null=True, blank=True)
    question3 = models.CharField(max_length=32, null=True, blank=True)
    question4 = models.CharField(max_length=32, null=True, blank=True)
    question5 = models.CharField(max_length=32, null=True, blank=True)
    question6 = models.CharField(max_length=32, null=True, blank=True)
    question7 = models.CharField(max_length=32, null=True, blank=True)
    question8 = models.CharField(max_length=32, null=True, blank=True)
    question9 = models.CharField(max_length=32, null=True, blank=True)
    question10 = models.CharField(max_length=32, null=True, blank=True)
