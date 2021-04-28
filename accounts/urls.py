from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    # profile
    path('<str:username>/', views.profile, name='profile'),
    # follow
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]