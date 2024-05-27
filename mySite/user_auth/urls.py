from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('user/', views.show_user, name='show_user'),
    path('register/', views.register_user, name='register'),  # Add URL pattern for register page
    path('logout/', views.user_logout, name='logout'),
]
