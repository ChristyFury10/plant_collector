from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('plants/', views.PlantList.as_view(), name="plant_list"),
    path('plants/new/', views.PlantCreate.as_view(), name="plant_create"),
    path('plants/<int:pk>/', views.PlantDetail.as_view(), name="plant_detail"),
    path('plants/<int:pk>/update', views.PlantUpdate.as_view(), name="plant_update"),
    path('plants/<int:pk>/delete', views.PlantDelete.as_view(), name="plant_delete_confirmation"),


]