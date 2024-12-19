# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # หน้าแรก
    path('next/', views.next_page, name='next_page'),  # หน้าถัดไป
]
