# Generated by Django 4.2.2 on 2023-07-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_tours', '0003_alter_tour_total_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='total_rating',
            field=models.BigIntegerField(default=0),
        ),
    ]