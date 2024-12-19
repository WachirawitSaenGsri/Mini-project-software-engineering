# main/views.py
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def next_page(request):
    return render(request, 'next_page.html')
