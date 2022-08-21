from django.urls import path

from . import views

urlpatterns = [
        path('', views.index),
        path('profile/', views.profile),
        path('user_register/<username>,<email>,<password>/', views.user_register),
        path('logout/', views.user_logout),
        path('add_interval/<start_date>, <end_date>', views.add_interval),
        path('auth/', views.auth),
        path('intervals/', views.intervals)
]
