from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

def home(request):
    return render(request, 'working/main.html')

def about(request):
    return render(request, 'working/about.html')

def courses(request):
    return render(request, 'working/courses.html')

def join(request):
    return render(request, 'working/join.html')

def pages_icons(request):
    return render(request, 'working/icons.html')

def pages_codes(request):
    return render(request, 'working/codes.html')

def gallery(request):
    return render(request, 'working/gallery.html')

def contact(request):
    return render(request, 'working/contact.html')

def login(request):
    return render(request, 'working/login.html')

def register(request):
    return render(request, 'working/register.html')

def Lecture_NP_1(request):
    return render(request, 'working/NP_1.html')

def Lecture_NP_2(request):
    return render(request, 'working/NP_2.html')

def Lecture_GS(request):
    return render(request, 'working/GS.html')