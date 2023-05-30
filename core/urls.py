from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('', include('tourplan.urls', namespace='tourplan')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('game/', include('game.urls', namespace='game')),
]
