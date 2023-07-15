from django.urls import path, re_path
from . import consumers

websocket_urlpatterns = [
    path('ws/<str:group_name>/', consumers.MyWebSocket.as_asgi())
]