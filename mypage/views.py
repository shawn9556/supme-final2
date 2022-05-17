from wsgiref.handlers import format_date_time
from django.shortcuts import render, redirect, get_object_or_404
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.contrib import auth
from mypage.models import Profile, Select
from travelbox.models import Travel_box, GetPic
from allauth.socialaccount import models
from django.utils import timezone
from survey.models import SurveyQuestion
from django.db.utils import OperationalError

from datetime import datetime


# Create your views here.

def index(request):
    return render(request, 'mypage/index.html')

### LOGIN ###
def login(request):
    context ={}
    if request.method == "POST":
        if request.POST.get('username') and request.POST.get('password'):
            user = auth.authenticate(
                request,
                username = request.POST.get('username'),
                password = request.POST.get('password'),
            )
            if user is not None:
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect("mypage:dashboard")
            else:
                context['error'] = '아이디와 비밀번호를 다시 확인해주세요'
        else:
            context['error'] = '아이디와 비밀번호를 다시 확인해주세요'
    return render(request, 'mypage/login.html', context)


### LOGOUT ###
def logout(request):
    if request.method == "POST":
        auth.logout(request)
    return redirect('mypage:home')


### SIGN UP ###
def signup(request):
    context = {}
    if request.method == "POST":
        if(request.POST.get('username') and
            request.POST.get('password') and
            request.POST.get('password') == request.POST.get('password_check')):
            new_user = User.objects.create_user(
                username = request.POST.get('username'),
                password = request.POST.get('password'),
            )
            # auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("mypage:signup_add_info")
        else:
            context["error"] = '올바르지 않은 정보입니다.'
    
    return render(request, 'mypage/sign_up.html')



####SIGN UP ADD INFO ####
def signup_add_info(request):
    if not request.user.is_authenticated:
        return redirect("mypage:login")

    if request.method == "GET":
        return signup_add_info_view(request)

    #### 홈페이지를 통해 회원 가입한 user의 추가 정보 ####
    # Form Element의 요청을 통해 받은 데이터 저장
    if request.method == "POST":
        new_profile = Profile()
        new_profile.gender = request.POST.get('gender')
        new_profile.name = request.POST.get('name')
        new_profile.phone_number = request.POST.get('phone_number')
        new_profile.age = request.POST.get('age')
        new_profile.email = request.POST.get('email')
        new_profile.for_user = request.user
        new_profile.save()
        return redirect('mypage:dashboard')
        # return redirect('mypage:dashboard', username = new_profile.for_user)



def signup_add_info_view(request):
    #### social login user profile ####
    context = {}
    survey_uid = request.COOKIES.get("supme-survey-id")
    user_gender = None
    user_age = None
    user_email = None

    # 소셜 계정이 있다면
    if SocialAccount.objects.filter(user=request.user).exists():
        # 소셜계정 가져오기
        social_user = SocialAccount.objects.get(user=request.user)
        # 소셜 계정의 성별 정보를 임시 저장
        user_gender = social_user.extra_data.get('gender')
        
        # 소셜 계정의 나이 정보를 임시 저장
        user_age = social_user.extra_data.get('age')
        if user_age is None:
            user_age = social_user.extra_data.get('age_range')

        # 소셜 계정의 이메일 정보를 임시 저장
        user_email = social_user.extra_data.get('email')


    # 회수한 성별 정보 있는지 확인 후 전달 (context["M"] or context["W"])
    if user_gender is None:
        try:
            user_gender_list = SurveyQuestion.objects.filter(survey_uid=survey_uid).order_by("-pk")[0]
            user_gender = user_gender_list.question2
        except OperationalError:
            pass

    if user_gender is not None:
        if user_gender == "M":
            context["M"] = True
        elif user_gender == "W":
            context["W"] = True

    # 회수한 나이 정보 있는지 확인 후 전달 (context["age"])
    if user_age is not None:
        context["age"] = user_age

    # 회수한 이메일 정보 있는지 확인 후 전달 (context["email"])
    if user_email is not None:
        context["email"] = user_email

    # (소셜 계정 및 Question2에서) 받은 데이터와 함깨 HTML전달
    return render(request, 'mypage/signup_add_info.html', context)




def dashboard(request):
    if request.user.is_authenticated:
        profile = Profile.objects.all().filter(for_user=request.user)
        box_viewer = Travel_box.objects.all().filter(travel_box_user=request.user)

        context = {}

        if len(profile) < 1:
            return redirect("mypage:signup_add_info")
        else:
            profile = profile[0]
            current_select_list = Select.objects.filter(selector=profile).exclude(selection_state="finished")

            ### 여행 의뢰 할 수 있도록 만드는 버튼 ####
            can_select = not current_select_list.exists()
            if not can_select:
                current_select = current_select_list.order_by("-pk")[0]
                context[current_select.selection_state] = True
           
            #### 유저의 해당 travelbox 보기 ####
            if box_viewer:
                box_viewer = box_viewer.order_by("-pk")[0]
                
                #### 유저가 사진 올린거 사진첩에 띄우기 ####
                album = GetPic.objects.filter(box_id=box_viewer.id).order_by("-pk")[0]
            
            context.update({
                "profile": profile,
                "can_select": can_select,
                "box_viewer": box_viewer,
                "album": album,
            })
            return render(request, 'mypage/dashboard.html', context)

    return redirect("mypage:home")
    

def select_travel(request):
    profile = get_object_or_404(Profile, for_user=request.user)
    print(request.POST.get("daterange"))
    daterange_raw = request.POST.get("daterange")
    date_start = daterange_raw.split(" - ")[0]
    date_end = daterange_raw.split(" - ")[1]

    date_start = datetime.strptime(date_start, "%m/%d/%Y")
    date_end = datetime.strptime(date_end, "%m/%d/%Y")

    select = Select(
        selector=profile, 
        people=request.POST.get('people'), 
        start_date=date_start,
        end_date=date_end,
        travel_purpose=request.POST.get('travel_purpose'), 
        place_start=request.POST.get('place_start'), 
        create_date=timezone.now()
        )
    select.save()
    return redirect("mypage:dashboard")


def update(request):
    if request.method == "GET":
        return render(request, "mypage/profile_update.html")
    elif request.method == "POST":
        profile_update = Profile.objects.get(for_user=request.user)
        profile_update.name = request.POST.get('name')
        profile_update.phone_number = request.POST.get('phone_number')
        profile_update.email = request.POST.get('email')
        profile_update.save()
    return redirect("mypage:dashboard")

