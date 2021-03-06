from django.urls import path
from . import views
app_name = 'instargram'

urlpatterns = [
    path('', views.first, name='first'),   
    path('index', views.index, name='index'), 
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),

    # Like
    path('<int:pk>/like/', views.like, name='like'),
    path('<int:pk>/detail_like/', views.detail_like, name='detail_like'),
]
