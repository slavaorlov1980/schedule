from django.http import JsonResponse, HttpResponse
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
    username = request_data["loginName"]
    password = request_data["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"Success": "Вы авторизованы", "username": user.username})
    else:
        return JsonResponse({"Error": "Данные некорректны"})

def check_auth(request):
    result = request.user.is_authenticated
    username = ''
    first_name = ''
    if result:
        username = request.user.username
        first_name = request.user.first_name
    return JsonResponse({'result': result, 'username': username, 'first_name': first_name})

def user_logout(request):
    logout(request)
    return JsonResponse({'Success': 'You\'re logged out'}) 


def submit_interval(request):

#    interval = Interval.objects.create(start_date=start_date, end_date=end_date)
    request_data = json.loads(request.body)
    data = request_data['schedule']
    print(f'{data = }')
    response_data = {'data': data}
    return JsonResponse(response_data)
