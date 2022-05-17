from django.shortcuts import render, redirect
from home.models import PotentialUser

# Create your views here.

def home(request):
    if request.method == "POST":
        poten_user_email = PotentialUser()
        poten_user_email.email = request.POST.get('email')
        poten_user_email.save()
    return render(request, 'home/index.html')