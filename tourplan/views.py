from django.shortcuts import render, redirect
from tourplan.models import *


def home_view(request):
    tourplans = TourPlace.objects.all().order_by('-id')[:5]
    hotels = Hotel.objects.all().order_by('-id')[:5]
    agencies = Agency.objects.all().order_by('-id')[:5]
    restaurants = Restaurant.objects.all().order_by('-id')[:5]
    context = {
        'tourplans': tourplans,
        'hotels': hotels,
        'agencies': agencies,
        'restaurants': restaurants,
    }
    return render(request, 'tourplan/home.html', context=context)


def tourplan_view(request, slug=None):
    tourplans = TourPlace.objects.all()
    if slug:
        tourplan = TourPlace.objects.filter(slug=slug)
        return render(request, 'tourplan/tourplan_list.html', {'tourplan': tourplan})
    else:
        return render(request, 'tourplan/tourplan_list.html', {'tourplans': tourplans})


def hotel_view(request):
    hotels = Hotel.objects.all()
    return render(request, 'tourplan/home.html', {'hotels': hotels})


def agency_view(request):
    agencies = Agency.objects.all()
    return render(request, 'tourplan/agency.html', {'agencies': agencies})


def restaurant_view(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'tourplan/restaurant.html', {'restaurants': restaurants})



