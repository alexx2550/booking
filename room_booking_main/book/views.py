from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking, Rooms, Hotel, Place
from datetime import datetime


def registration_list(request):
    bookings = Booking.objects.all()
    return render(request, 'book/registration_list.html', {'bookings': bookings})

def registration_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'book/registration_detail.html', {'booking': booking})

def book_room(request):
    room_choices = Rooms.objects.all()
    hotel_choices = Hotel.objects.all()
    place_choices = Place.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        check_in_str = request.POST.get('check_in')
        check_out_str = request.POST.get('check_out')
        check_in = datetime.strptime(check_in_str, '%Y-%m-%dT%H:%M')
        check_out = datetime.strptime(check_out_str, '%Y-%m-%dT%H:%M')
        phone_number = request.POST.get('phone_number')
        room_type_id = request.POST.get('room_type')
        place_id = request.POST.get('place')
        hotel_id = request.POST.get('hotel')


        booking = Booking(
            name=name,
            surname=surname,
            check_in=check_in,
            check_out=check_out,
            phone_number=phone_number,
            room_type_id=room_type_id,
            place_id=place_id,
            hotel_id=hotel_id,
        )

        booking.calculate_total_price()

        booking.save()


        return redirect('book:registration_list')      
        
    return render(request, 'book/book_room.html', {'hotel_choices': hotel_choices, 'place_choices': place_choices,'room_choices': room_choices})
