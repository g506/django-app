from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from framework.utils import SOCIAL_PROFILE_PLATFORMS

from framework.validators import validate_file_size, processed_image_field_specs
from imagekit.models import ProcessedImageField
import datetime
import uuid


class Tags(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Tags"
        verbose_name = "Tag"

    def __str__(self):
        return self.name

class Interests(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Interests"
        verbose_name = "Interest"

    def __str__(self):
        return self.name


class User(AbstractUser):
    def get_avatar_path(self, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return 'static/uploads/images/avatar/' + filename

    INTEREST_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
    )
    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
        (2, 'Other'),
    )
    id = models.BigAutoField(primary_key=True, null=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=255, default='', blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=255, default='', blank=True, verbose_name='Last Name')
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    user_type = models.CharField(max_length=100)
    bio = models.CharField(max_length=255, default='', blank=True, verbose_name='Bio')
    url = models.URLField(max_length=255, default='', blank=True, verbose_name='URL')
    location = models.CharField(max_length=255, default='', blank=True)
    country = models.CharField(max_length=10, null=False, blank=False, default='IND')
    birthday = models.DateField(null=False, default = datetime.date.today)
    isOnline = models.BooleanField(default=False)
    familyPlans = models.CharField(null=True, max_length=200)
    tags = models.ManyToManyField(Tags, related_name='profile_tags')
    politics = models.CharField(max_length=200)
    coins = models.IntegerField(null=False,default=0)
    zodiacSign = models.CharField(max_length=200)
    height = models.IntegerField(null=False,default=0)
    interestedIn = models.ManyToManyField(Interests, blank=True,related_name='interest')
    payment_method = models.CharField(max_length=10)
    
    avatar = ProcessedImageField(
        blank=True,
        verbose_name='Avatar',
        upload_to=get_avatar_path,
        null=True,
        validators=[validate_file_size],
        **processed_image_field_specs
    )

class UserSocialProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.PositiveSmallIntegerField(choices=SOCIAL_PROFILE_PLATFORMS, default=4)
    url = models.URLField()

    class Meta:
        verbose_name_plural = "User Social Profiles"
        verbose_name = "User Social Profile"

    def __str__(self):
        return str(self.user.username) + ' - ' + str(self.platform)

