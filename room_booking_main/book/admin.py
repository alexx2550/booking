from django.contrib import admin
from .models import Booking, Rooms, Hotel, Place

admin.site.register(Booking)

@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('room_type',)

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel',)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place',)
