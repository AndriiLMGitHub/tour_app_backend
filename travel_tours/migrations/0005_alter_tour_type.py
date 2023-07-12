# Generated by Django 4.2.2 on 2023-07-12 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_tours', '0004_alter_tour_total_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='travel_tours.tourtype'),
        ),
    ]