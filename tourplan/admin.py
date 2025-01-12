from django.contrib import admin
from tourplan.models import *


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('district', 'division')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TourPlace)
class TourPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'address')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'weblink')


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'weblink')


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'weblink', 'image')

