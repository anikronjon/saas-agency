from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.post_list_detail, name='post_list'),
    path('', views.post_list_detail, name='post_detail'),
]