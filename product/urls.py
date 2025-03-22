from django.urls import path

from .views import *

urlpatterns = [
    path('', PlantAPIView.as_view(), name='plant_list'),
    path('<int:id>/', PlantDetailAPIView.as_view(), name='plant_detail'),
    path('category/', PlantFilter, name='plant_filter'),


]