# Generated by Django 4.2.4 on 2023-10-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_roomtype_alter_booking_room_type_delete_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='room_type',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='RoomType',
        ),
    ]