from django.db import models


class Hotel(models.Model):
    HOTEL_1 = 'Radisson BLU Hotel'
    HOTEL_2 = 'Ani Plasa Hotel'
    HOTEL_3 = 'The Alexander Hotel'
    HOTEL_4 = 'Tufenkian Historic Yerevan Hotel'

    HOTEL_CHOICE = [
        (HOTEL_1, 'Radisson BLU Hotel'),
        (HOTEL_2, 'Ani Plaza Hotel'),
        (HOTEL_3, 'The Alexander Hotel'),
        (HOTEL_4, 'Tufenkian Historic Yerevan Hotel'),
    ]

    hotel = models.CharField(max_length=100, choices=HOTEL_CHOICE, null=True)

    def __str__(self):
        return self.get_hotel_display()


class Place(models.Model):
    PLACE_1 = 'Yerevan'

    PLACE_CHOICE = [
        (PLACE_1, 'Yerevan'),
    ]

    place = models.CharField(max_length=100, choices=PLACE_CHOICE, null=True)

    def __str__(self):
        return self.get_place_display()
   

class Rooms(models.Model):
    SINGLE = 'Single'
    DOUBLE = 'Double'
    DELUXE = 'Deluxe'
    PRESIDENTIAL = 'Presidential'

    ROOM_TYPE_CHOICES = [
        (SINGLE, 'Single Room'),
        (DOUBLE, 'Double Room'),
        (DELUXE, 'Deluxe Room'),
        (PRESIDENTIAL, 'Presidential Room'),
    ]

    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES, null=True)

    def __str__(self):
        return self.get_room_type_display()

    def get_room_price(self):
        room_prices = {
            Rooms.SINGLE: 150,
            Rooms.DOUBLE: 280,
            Rooms.DELUXE: 400,
            Rooms.PRESIDENTIAL: 750,
        }
        return room_prices.get(self.room_type, 0)
    

class Booking(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True)
    phone_number = models.CharField(max_length=20)
    room_type = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  

    def __str__(self):
        return f'{self.name} {self.surname}'

    def calculate_total_price(self):
        if self.check_in and self.check_out and self.room_type:
            duration = (self.check_out - self.check_in).days
            room_price = self.room_type.get_room_price()
            total_price = room_price * duration
            self.price = total_price
            self.save()

        return self.price
