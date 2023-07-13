from django.urls import path
from . import views

app_name = 'tourplan'
urlpatterns = [
    path('', views.home_view, name='home_page'),
    path('tour/', views.tourplan_view, name='tourplan_list_page'),
    path('tour/<slug:slug>/', views.tourplan_view, name='tourplan_detail_page'),

    path('agency/', views.agency_view, name='agency_list_page'),
    path('hotel/', views.hotel_view, name='hotel_list_page'),
    path('restaurant/', views.restaurant_view, name='restaurant_list_page'),
    path('about/', views.about_view, name='about_page'),
    path('contact/', views.contact_view, name='contact_page'),
]
