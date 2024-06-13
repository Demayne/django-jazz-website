# urls.py
from django.urls import path
from .views import contact_us, contact_success
from . import views

app_name = 'contact'  # Set the app_name attribute'

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('contact/success/', views.contact_success, name='contact_success'),
    
]
