from django.urls import path

from . import views

urlpatterns = [
        path('', views.index),
        path('profile/', views.profile),
        path('user_register/<username>,<email>,<password>/', views.user_register),
        path('logout/', views.user_logout),
        path('auth/', views.auth),
        path('submit_interval/', views.submit_interval),
        path('check_auth/', views.check_auth)
]
