# Generated by Django 4.2.4 on 2023-11-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_alter_hotel_hotel_alter_place_place_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
