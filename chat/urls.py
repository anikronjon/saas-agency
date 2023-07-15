from django.urls import path
from . import views


app_name = 'chat'
urlpatterns = [
    path('group/', views.message_group_view, name='group_page'),
    path('group/<str:group_name>/', views.message_chat_view, name='chat_page'),
]