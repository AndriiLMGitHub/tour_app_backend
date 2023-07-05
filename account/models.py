from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.conf import settings


# User Model
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("Email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# Profile Model
class Profile(models.Model):
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    sex = models.CharField(max_length=20, choices=CHOICES)
    name = models.CharField(max_length=255)
    date_birth = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=120)
    bio = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'User profile - {self.user.email}'

    class Meta:
        verbose_name = "User Profile"


class UserProfileImage(models.Model):
    user_id = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='profile_images'
    )
    avatar = models.FileField(
        upload_to='user/avatars/',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Avatar - {self.user_id.user}'

    class Meta:
        verbose_name = "User Profile Image"


# User Host Model
class UserHost(models.Model):
    user_id = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='host'
    )
    is_host = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    telephone = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "User Host"

    def __str__(self):
        return f'Host with email - {self.user_id.email}'


class UserHostPassportImage(models.Model):
    user_id = models.ForeignKey(
        UserHost,
        on_delete=models.CASCADE,
        related_name='host_passport_images'
    )
    passport_photos = models.FileField(
        upload_to='user/passports/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "User Host Passport Image"

    def __str__(self):
        return f'Passpost image - {self.user_id.user_id}'


class SocialUser(models.Model):
    TYPES = (
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('LinkedIn', 'LinkedIn'),
        ('Youtube', 'Youtube'),
    )
    user_profile_id = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='socials'
    )
    facebook = models.URLField(max_length=255)
    instagram = models.URLField(max_length=255)
    youtube = models.URLField(max_length=255)
    linked_in = models.URLField(max_length=255)

    class Meta:
        verbose_name = "User Social"

    def __str__(self):
        return f'Social {self.user_profile_id.user} - {self.type}'


# Signal to create Profile and Host models on user creation
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        UserHost.objects.create(user_id=instance)


# def create_user_host_passport_images(sender, instance, created, **kwargs):
#     if created:
#         UserHostPassportImage.objects.create(user_id=instance)


post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
# post_save.connect(create_user_host_passport_images, sender=UserHost)
