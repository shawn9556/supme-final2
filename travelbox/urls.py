from django.urls import path

from travelbox import views


app_name='travelbox'

urlpatterns = [
    # path("create/", views.create, name="create"),
    path("create/<int:selection_id>/", views.create, name="create_tmp"),
    path('read/<int:post_id>/', views.read, name='read_box'),
    path('read-all/', views.read_all, name='read_all'),
    path('update/<int:post_id>/', views.box_update, name='box_update'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('weather/', views.weather, name='weather'),
    path('travelbox/<int:post_id>/', views.travelbox, name='travelbox'),
    # path('travelbox/<str:travel_box_user>', views.travelbox, name='travelbox'),



]