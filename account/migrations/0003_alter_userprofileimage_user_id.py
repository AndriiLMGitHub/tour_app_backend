# Generated by Django 4.2.2 on 2023-06-26 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_user_userhostpassportimage_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileimage',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_image', to='account.profile'),
        ),
    ]
