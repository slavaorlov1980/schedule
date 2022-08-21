from django.http import JsonResponse
from .models import Profile, Interval, Event
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
import json

def index(request):
    return render(request, 'lessons/index.html')

def profile(request):
    return render(request, 'lessons/profile.html')

def user_register(request, username, email, password):
    response_data={}

    if User.objects.filter(username=username):
        response_data['error'] = f'User name \'{username}\' already exists'
    else:
        user = User.objects.create_user(username, email, password)
        user.save()
        response_data['result'] = f'User \'{username}\' succesfully registered'
        

    return JsonResponse(response_data)
    
def auth(request):
    request_data = json.loads(request.body)
    username = request_data["username"]
    password = request_data["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"Success" : "Вы авторизованы"})
    else:
        return JsonResponse({"Error" : "Данные некорректны"})


def user_logout(request):
    logout(request)
    return JsonResponse({'Success' : 'You\'re logged out'}) 

def intervals(request):
    response_data = []
    intervals_data = Interval.objects.all()
    date = '21.08.2022'
    time = '14:00 - 15:00'
    response_data = {'date': date, 'time': time}
    return JsonResponse(response_data)

def add_interval(request, start_date, end_date):
#    interval = Interval.objects.create(start_date=start_date, end_date=end_date)
    pass
