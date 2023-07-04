from django.urls import path
from . import views

app_name = 'tourplan'
urlpatterns = [
    path('', views.home_view, name='home_page'),
    path('agency/', views.agency_view, name='agency_page'),
    path('hotel/', views.hotel_view, name='hotel_page'),
    path('restaurant/', views.restaurant_view, name='restaurant_page'),
]
