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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    sex = models.CharField(max_length=20, choices=CHOICES)
    date_birth = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=120)
    bio = models.TextField(null=True, blank=True)
    avatar = models.FileField(upload_to='user/avatars/', null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'User profile with email - {self.user.email}'

    class Meta:
        verbose_name = "User Profile"


# User Host Model
class UserHost(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='host')
    is_host = models.BooleanField(default=False)
    telephone = models.PositiveIntegerField(null=True, blank=True)
    passport_photos = models.FileField(upload_to='user/passports/', null=True, blank=True)

    class Meta:
        verbose_name = "User Host"


# Signal to create Profile and Host models on user creation
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        UserHost.objects.create(user_id=instance)


post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
