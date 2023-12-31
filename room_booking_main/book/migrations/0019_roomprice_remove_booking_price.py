# Generated by Django 4.2.4 on 2023-11-03 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_booking_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_price_choice', models.CharField(choices=[(180, '180$'), (300, '300$'), (500, '500$'), (850, '850$')], default=True, max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='price',
        ),
    ]
