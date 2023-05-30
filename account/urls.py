from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('profile/', views.profile_view, name='profile')
]