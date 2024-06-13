from django.urls import path
from .views import about_view, childhood1_view, javaScript_view

urlpatterns = [
    path('about/', about_view, name='about'),
    path('childhood1/', childhood1_view, name='childhood1'),
    path('javaScript/', javaScript_view, name='javaScript')

    
]

#Each of the html files once rendered will display on the localhost urls below

# http://localhost:8000/personal/about/ to view about information
# http://localhost:8000/personal/childhood1/ to view childhood information
# http://localhost:8000/personal/javaScript/ to view javaScript resource information