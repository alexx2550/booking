# Generated by Django 4.2.4 on 2023-10-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_booking_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='room_type',
            field=models.CharField(choices=[('Single', 'Single Room'), ('Double', 'Double Room'), ('Deluxe', 'Deluxe Room'), ('Presidential', 'Presidential Room')], max_length=20, null=True),
        ),
    ]