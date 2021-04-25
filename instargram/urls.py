from django.urls import path
from . import views
app_name = 'instargram'

urlpatterns = [
    path('', views.first, name='first'),   
    path('index', views.index, name='index'), 
]
