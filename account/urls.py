from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login
    path('login/',
         auth_views.LoginView.as_view(),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('',
         views.dashboard,
         name='dashboard'),
    path('',
         include('django.contrib.auth.urls')),
    # Registration
    path('register/',
         views.register,
         name='register'),
]
