from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    # path('<slug:slug>/like/', views.like_post, name='post_like'),
    # path('<slug:slug>/comment/', views.comment_post, name='post_comment'),
    # path('<slug:slug>/rate/', views.rating_post, name='post_rate'),
]
