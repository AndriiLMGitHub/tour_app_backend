# Generated by Django 4.2.2 on 2023-07-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='User without username', max_length=255),
        ),
    ]