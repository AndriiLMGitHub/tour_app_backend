# Generated by Django 4.2.2 on 2023-07-18 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=120)),
                ('city_image', models.FileField(upload_to='city/images/')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cites',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('date_start', models.DateTimeField()),
                ('date_finish', models.DateTimeField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('languages', models.CharField(max_length=120)),
                ('longitude', models.CharField(max_length=120)),
                ('latitude', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('price', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('total_rating', models.BigIntegerField(default=0)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours', to='travel_tours.city')),
            ],
        ),
        migrations.CreateModel(
            name='TourType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_images', models.FileField(blank=True, null=True, upload_to='tours/images/')),
                ('tour_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='travel_tours.tour')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_tours.tourtype'),
        ),
        migrations.AddField(
            model_name='tour',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours', to='account.userhost'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='travel_tours.tour')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('tour_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='travel_tours.tour')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
