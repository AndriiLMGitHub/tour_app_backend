# Generated by Django 4.2.2 on 2023-07-18 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_tours', '0002_comment_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=255)),
            ],
        ),
    ]
