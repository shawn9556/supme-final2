from time import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect
from mypage.models import Select
from django.utils import timezone

from travelbox.models import *
import requests
from .forms import CityForm

# Create your views here.

# def create(request, selection_id):
#     target_selection = Select.objects.get(id=selection_id)
#     # target_selection.selector.for_user
#     if request.method == 'GET':
#         return render(request, 'travelbox/box_create.html', context={
#             "selection": target_selection
#         })
#     elif request.method =='POST':
#         mk_box = Travel_box()
       
#         # mk_box.id = request.POST['id']
#         mk_box.travel_box_user = request.POST.get(user=target_selection.selector.for_user)

#         #### 우리가 travelbox 제작 ####
#         mk_box.sub_title = request.POST.get('sub_title')
#         mk_box.script = request.POST.get('script')
#         mk_box.place_name = request.POST.get("place_name")
#         mk_box.activity = request.POST.get('activity')
#         mk_box.accomdation = request.POST.get('accomdation')
#         mk_box.addr_accomdation = request.POST.get('addr_accomdation')
#         mk_box.food = request.POST.get('food')      
#         mk_box.sightseeing = request.POST.get('sightseeing')      
#         # mk_box.sightseeing_addr_link = request.POST.get('sightseeing_addr_link')      
#         mk_box.traffic = request.POST.get('traffic')

#         ### 장소 이미지 ###
#         if request.FILES.get("image_head"):          
#             mk_box.image_head = request.FILES['image_head']
        
#         ### 미션 이미지 ###
#         if request.FILES.get("image_1"):          
#             mk_box.image_1 = request.FILES['image_1']
#         if request.FILES.get("image_2"):  
#             mk_box.image_2 = request.FILES['image_2']
#         if request.FILES.get("image_3"):  
#             mk_box.image_3 = request.FILES['image_3']

#         ### 숙소, 음식, 액티비티, 볼거리 이미지 ###
#         if request.FILES.get("image_accomdation"):          
#             mk_box.image_accomdation = request.FILES['image_accomdation']
#         if request.FILES.get("image_food"):          
#             mk_box.image_food = request.FILES['image_food']
#         if request.FILES.get("image_activity"):          
#             mk_box.image_activity = request.FILES['image_activity']
#         if request.FILES.get("image_sightseeing"):          
#             mk_box.image_sightseeing = request.FILES['image_sightseeing']

#         ### 우리가 장소를 선택안하는 문제 방지 ###
#         if mk_box.place_name == "none":
#             return redirect("travelbox:create", selection_id)  
#         mk_box.save()
           
#         return redirect("travelbox:home")


### travel box 만들기 ###
def create(request, selection_id):
    target_selection = Select.objects.get(id=selection_id)
    if request.method == 'GET':
        return render(request, 'travelbox/box_create.html', context={
            "selection": target_selection
        })
    elif request.method =='POST':
        mk_box = Travel_box()
       
        # mk_box.id = request.POST['id']
        mk_box.travel_box_user = target_selection.selector.for_user
        mk_box.travel_box_id = target_selection
        #### 우리가 travelbox 제작 ####
        mk_box.sub_title = request.POST.get('sub_title')
        mk_box.script = request.POST.get('script')
        mk_box.place_name = request.POST.get("place_name")

        mk_box.activity_1 = request.POST.get('activity_1')
        mk_box.activity_2= request.POST.get('activity_2')
        mk_box.activity_3 = request.POST.get('activity_3')
        
        mk_box.addr_activity_1 = request.POST.get('addr_activity_1')
        mk_box.addr_activity_2= request.POST.get('addr_activity_2')
        mk_box.addr_activity_3 = request.POST.get('addr_activity_3')

        mk_box.accomdation_1 = request.POST.get('accomdation_1')
        mk_box.accomdation_2 = request.POST.get('accomdation_2')
        mk_box.accomdation_3 = request.POST.get('accomdation_3')
       
        mk_box.addr_accomdation_1 = request.POST.get('addr_accomdation_1')
        mk_box.addr_accomdation_2 = request.POST.get('addr_accomdation_2')
        mk_box.addr_accomdation_3 = request.POST.get('addr_accomdation_3')

        mk_box.food_1 = request.POST.get('food_1')      
        mk_box.food_2 = request.POST.get('food_2')      
        mk_box.food_3 = request.POST.get('food_3')   
        
        mk_box.addr_food_1 = request.POST.get('addr_food_1')      
        mk_box.addr_food_2 = request.POST.get('addr_food_2')      
        mk_box.addr_food_3 = request.POST.get('addr_food_3')   

        mk_box.sightseeing_1 = request.POST.get('sightseeing_1')      
        mk_box.sightseeing_2 = request.POST.get('sightseeing_2')      
        mk_box.sightseeing_3 = request.POST.get('sightseeing_3')      
        
        mk_box.addr_sightseeing_1 = request.POST.get('sightseeing_1')      
        mk_box.addr_sightseeing_2 = request.POST.get('sightseeing_2')      
        mk_box.addr_sightseeing_3 = request.POST.get('sightseeing_3')      
        

        mk_box.traffic = request.POST.get('traffic')
        mk_box.create_date = timezone.now()

        ### 장소 이미지 ###
        if request.FILES.get("image_head"):          
            mk_box.image_head = request.FILES['image_head']
        
        ### 미션 이미지 ###
        if request.FILES.get("image_1"):          
            mk_box.image_1 = request.FILES['image_1']
        if request.FILES.get("image_2"):  
            mk_box.image_2 = request.FILES['image_2']
        if request.FILES.get("image_3"):  
            mk_box.image_3 = request.FILES['image_3']

        ### 숙소, 음식, 액티비티, 볼거리 이미지 ###
        if request.FILES.get("image_accomdation_1"):          
            mk_box.image_accomdation_1 = request.FILES['image_accomdation_1']
        if request.FILES.get("image_accomdation_2"):          
            mk_box.image_accomdation_2 = request.FILES['image_accomdation_2']
        if request.FILES.get("image_accomdation_3"):          
            mk_box.image_accomdation_3 = request.FILES['image_accomdation_3']

        if request.FILES.get("image_food_1"):          
            mk_box.image_food_1 = request.FILES['image_food_1']
        if request.FILES.get("image_food_2"):          
            mk_box.image_food_2 = request.FILES['image_food_2']
        if request.FILES.get("image_food_3"):          
            mk_box.image_food_3 = request.FILES['image_food_3']

        if request.FILES.get("image_activity_1"):          
            mk_box.image_activity_1 = request.FILES['image_activity_1']
        if request.FILES.get("image_activity_2"):          
            mk_box.image_activity_2 = request.FILES['image_activity_2']
        if request.FILES.get("image_activity_3"):          
            mk_box.image_activity_3 = request.FILES['image_activity_3']

        if request.FILES.get("image_sightseeing_1"):          
            mk_box.image_sightseeing_1 = request.FILES['image_sightseeing_1']
        if request.FILES.get("image_sightseeing_2"):          
            mk_box.image_sightseeing_2 = request.FILES['image_sightseeing_2']
        if request.FILES.get("image_sightseeing_3"):          
            mk_box.image_sightseeing_3 = request.FILES['image_sightseeing_3']
        
        if request.FILES.get("traffic_road"):          
            mk_box.traffic_road = request.FILES['traffic_road']





        ### 우리가 장소를 선택안하는 문제 방지 ###
        if mk_box.place_name == "none":
            return redirect("travelbox:create")   
        mk_box.save()
        # print(selection_id)
        # return render(request, 'travelbox/box_create.html')
        return redirect("travelbox:read_all")


 ### 해당 유저의 travel box를 우리가 잘 만들었는지 우리측 확인용(travel box error 여부 확인용) ###
def read(request, post_id):

    post = Travel_box.objects.get(id=post_id)

    context = {
        'post': post,
        
        
    }

    return render(request, 'travelbox/read_box.html', context)


### 우리가 만든 travel box들에 대한 리스트 ###
def read_all(request):
    
    post_list = Travel_box.objects.all()

    context = {
        'posts': post_list
        
    }

    return render(request, 'travelbox/read_box_list.html', context)

### travel box 수정 ###
def box_update(request, post_id):
    if request.method =='GET':
            
        post =Travel_box.objects.get(id = post_id)
        context = {
            'post' : post
        }
        return render(request, "travelbox/box_update.html", context)


    elif request.method =='POST':
        target_post = Travel_box.objects.get(id = post_id)
        target_post.place_name = request.POST['place_name']
        target_post.traffic = request.POST['traffic']
        target_post.accomdation = request.POST['accomdation']
        target_post.food = request.POST['food']
        target_post.activity = request.POST['activity']
        target_post.sightseeing = request.POST['sightseeing']
        if request.FILES.get("image_1"):
            print('ok')
            target_post.image_1 = request.FILES['image_1']
        if request.FILES.get("image_2"):
            print('ok')
            target_post.image_2 = request.FILES['image_2']
        if request.FILES.get("image_3"):
            print('ok')
            target_post.image_3 = request.FILES['image_3']
        target_post.save()
        
        


        return HttpResponseRedirect('/travelbox/read-all/')

### travel box 자체를 삭제하기 ###
def delete(request, post_id):
    if request.method == "GET":
        post = Travel_box.objects.get(id = post_id)
        context = {
            'post' : post
        }
        return render(request, 'travelbox/box_delete.html', context)
    elif request.method == 'POST':
        delete_post = Travel_box.objects.get(id = post_id)
        delete_post.delete()
        return HttpResponseRedirect('/travelbox/read-all/')


### 날씨 정보 우리가 가져오기 ###
def weather(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5054f8884263db59d70b67fc83db029e'

    cities = City.objects.all() #return all the cities in the database
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save()
    
    form = CityForm()
    weather_data = []


    for city in cities:
        response = requests.get(url.format(city))
        if response.status_code != 200:
            print(city)
            continue
        city_weather = response.json() #request the API data and convert the JSON to Python data types
        print(f"city: {city}")
        # for key, value in city_weather.items():
        #     print(f"{key}: {value}")

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'travelbox/weather.html', context) #returns the index.html te






### User가 보는 travel box ###
def travelbox(request, post_id):
    read = Travel_box.objects.get(id = post_id)
    if read.travel_box_user != request.user:
        return redirect("mypage:dashboard")

    context = {
        'post': read, 
    
    }
        
    if request.method =='POST':
        # print("here")
    
        get_pic = GetPic()
        get_pic.box_id = read
        get_pic.checked = request.POST['checked']
        if request.FILES.get("user_image_1"):          
            get_pic.user_image_1 = request.FILES['user_image_1']
        if request.FILES.get("user_image_2"):  
            get_pic.user_image_2 = request.FILES['user_image_2']
        if request.FILES.get("user_image_3"):  
            get_pic.user_image_3 = request.FILES['user_image_3']
        #  if request.FILES.get("image_accomdation"):  
        #     get_pic.image_accomdation = request.FILES['image_accomdation']
        #  if request.FILES.get("image_food"):  
        #     get_pic.image_food = request.FILES['image_food']
        #  if request.FILES.get("image_activity"):  
        #     get_pic.image_activity = request.FILES['image_activity']
        #  if request.FILES.get("image_sightseeing"):  
        #     get_pic.image_sightseeing = request.FILES['image_sightseeing']
        #  if request.FILES.get("image_"):  
        #     get_pic.image_ = request.FILES['image_']
         
        get_pic.save()

        return render(request, "travelbox/mybox_submit_results.html", {
            "success": True,
        })

    return render(request, "travelbox/travelbox.html", context)
    




#     ### User가 보는 travel box ###
# def travelbox(request):
#     read = Travel_box.objects.all().filter(travel_box_user=request.user)
#     if read.travel_box_user != request.user:
#         return redirect("mypage:home")

#     context = {
#         'post': read, 
    
#     }
        
#     if request.method =='POST':
#         # print("here")
    
#         get_pic = GetPic()
#         get_pic.box_id = read

#         if request.FILES.get("user_image_1"):          
#             get_pic.user_image_1 = request.FILES['user_image_1']
#         if request.FILES.get("user_image_2"):  
#             get_pic.user_image_2 = request.FILES['user_image_2']
#         if request.FILES.get("user_image_3"):  
#             get_pic.user_image_3 = request.FILES['user_image_3']
#         #  if request.FILES.get("image_accomdation"):  
#         #     get_pic.image_accomdation = request.FILES['image_accomdation']
#         #  if request.FILES.get("image_food"):  
#         #     get_pic.image_food = request.FILES['image_food']
#         #  if request.FILES.get("image_activity"):  
#         #     get_pic.image_activity = request.FILES['image_activity']
#         #  if request.FILES.get("image_sightseeing"):  
#         #     get_pic.image_sightseeing = request.FILES['image_sightseeing']
#         #  if request.FILES.get("image_"):  
#         #     get_pic.image_ = request.FILES['image_']
         
#         get_pic.save()

#         return render(request, "travelbox/mybox_submit_results.html", {
#             "success": True,
#         })

#     return render(request, "travelbox/travelbox.html", context)