# Generated by Django 4.2.2 on 2023-07-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialuser',
            name='facebook',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='instagram',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='linked_in',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='youtube',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]