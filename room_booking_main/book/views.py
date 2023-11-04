from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking, Rooms, Hotel, Place

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
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        phone_number = request.POST.get('phone_number')
        room_type_id = request.POST.get('room_type')
        place_id = request.POST.get('place')
        hotel_id = request.POST.get('hotel')

        selected_room = get_object_or_404(Rooms, pk=room_type_id)
        room_price = selected_room.get_room_price()

        booking = Booking(
            
            name=name,
            surname=surname,
            check_in=check_in,
            check_out=check_out,
            phone_number=phone_number,
            room_type_id=room_type_id,
            place_id=place_id,
            hotel_id=hotel_id,
            price=room_price,
        )
        booking.save()


        return redirect('book:registration_list')      
        
    return render(request, 'book/book_room.html', {'hotel_choices': hotel_choices, 'place_choices': place_choices,'room_choices': room_choices})
