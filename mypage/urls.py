from django.urls import path
from mypage import views

app_name = 'mypage'

urlpatterns = [
    path('home/', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signup-add-info/', views.signup_add_info, name='signup_add_info'),
    path('select-travel/', views.select_travel, name='select_travel'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("update/",views.update, name="update"),

]