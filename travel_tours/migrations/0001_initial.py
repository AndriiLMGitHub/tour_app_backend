# Generated by Django 4.2.2 on 2023-07-02 12:54

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
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('type', models.CharField(choices=[('Backpaking', 'Backpaking'), ('Weekend', 'Weekend'), ('Adventure', 'Adventure'), ('Solo', 'Solo')], max_length=120)),
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
                ('rating', models.BigIntegerField(default=0)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours', to='travel_tours.city')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours', to='account.userhost')),
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
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tour_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='travel_tours.tour')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
