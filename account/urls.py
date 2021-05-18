from django.urls import path
from . import views

url_patterns = [
    # post views
    path('login/', views.user_login, name='login'),
]
