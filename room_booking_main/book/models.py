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


class RoomPrice(models.Model):
    SINGLE_PRICE = '180$'
    DOUBLE_PRICE = '300$'
    DELUXE_PRICE = '500$'
    PRESIDENTAL_PRICE = '850$'

    PRICE_CHOICE = [
        (SINGLE_PRICE, '180$'),
        (DOUBLE_PRICE, '300$'),
        (DELUXE_PRICE, '500$'),
        (PRESIDENTAL_PRICE, '850$'),
    ]

    room_price = models.CharField(max_length=50, choices=PRICE_CHOICE, null=True)

    def __str__(self):
        return self.get_room_price_display()


class Booking(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True)
    phone_number = models.CharField(max_length=20)
    room_type = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    room_price = models.ForeignKey(RoomPrice, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
