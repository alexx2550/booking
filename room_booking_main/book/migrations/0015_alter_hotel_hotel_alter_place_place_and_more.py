# Generated by Django 4.2.4 on 2023-10-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_alter_booking_hotel_alter_booking_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel',
            field=models.CharField(choices=[('', ''), ('Radisson BLU Hotel', 'Radisson BLU Hotel'), ('Ani Plasa Hotel', 'Ani Plaza Hotel'), ('The Alexander Hotel', 'The Alexander Hotel'), ('Tufenkian Historic Yerevan Hotel', 'Tufenkian Historic Yerevan Hotel')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='place',
            field=models.CharField(choices=[('', ''), ('Yerevan', 'Yerevan')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='room_type',
            field=models.CharField(choices=[('', ''), ('Single', 'Single Room'), ('Double', 'Double Room'), ('Deluxe', 'Deluxe Room'), ('Presidential', 'Presidential Room')], max_length=20, null=True),
        ),
    ]
