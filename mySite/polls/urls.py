from django.urls import path
from . import views
from user_auth.views import user_logout

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('logout/', user_logout, name='logout'), # Added logout path for the logout buttons
]
 