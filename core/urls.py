from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', include('tourplan.urls', namespace='tourplan')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('game/', include('game.urls', namespace='game')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)