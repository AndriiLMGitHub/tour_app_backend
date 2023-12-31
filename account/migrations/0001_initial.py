# Generated by Django 4.2.2 on 2023-07-18 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('date_birth', models.DateTimeField(blank=True, null=True)),
                ('address', models.CharField(max_length=120)),
                ('bio', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
            },
        ),
        migrations.CreateModel(
            name='UserHost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_host', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
                ('telephone', models.PositiveIntegerField(blank=True, null=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='host', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Host',
            },
        ),
        migrations.CreateModel(
            name='UserProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.FileField(blank=True, null=True, upload_to='user/avatars/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_images', to='account.profile')),
            ],
            options={
                'verbose_name': 'User Profile Image',
            },
        ),
        migrations.CreateModel(
            name='UserHostPassportImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_photos', models.FileField(blank=True, null=True, upload_to='user/passports/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_passport_images', to='account.userhost')),
            ],
            options={
                'verbose_name': 'User Host Passport Image',
            },
        ),
        migrations.CreateModel(
            name='SocialUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, max_length=255, null=True)),
                ('instagram', models.URLField(blank=True, max_length=255, null=True)),
                ('youtube', models.URLField(blank=True, max_length=255, null=True)),
                ('linked_in', models.URLField(blank=True, max_length=255, null=True)),
                ('user_profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socials', to='account.profile')),
            ],
            options={
                'verbose_name': 'User Social',
            },
        ),
    ]
