from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from framework.utils import SOCIAL_PROFILE_PLATFORMS

from framework.validators import validate_file_size, processed_image_field_specs
from imagekit.models import ProcessedImageField
import datetime
import uuid

RATING_TYPE = (('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'))

class User(AbstractUser):
    def get_avatar_path(self, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return 'static/uploads/images/avatar/' + filename

    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
        (2, 'Other'),
    )
    id = models.BigAutoField(primary_key=True, null=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    isEmailVerified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, default='', blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=255, default='', blank=True, verbose_name='Last Name')
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    user_type = models.CharField(max_length=100)
    bio = models.CharField(max_length=255, default='', blank=True, verbose_name='Bio')
    url = models.URLField(max_length=255, default='', blank=True, verbose_name='URL')
    location = models.CharField(max_length=255, default='', blank=True)
    country = models.CharField(max_length=10, null=False, blank=False, default='IND')
    birthday = models.DateField(null=False, default = datetime.date.today)
    isServiceProvider = models.BooleanField(default=True)
    avatar = ProcessedImageField(
        blank=True,
        verbose_name='Avatar',
        upload_to=get_avatar_path,
        null=True,
        validators=[validate_file_size],
        **processed_image_field_specs
    )

class Follow(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    followers = models.IntegerField()
    followings = models.IntegerField()
    class Meta:

        verbose_name_plural = "follow"
        verbose_name = "follow"

    def __str__(self):
        return str(self.username) + ' - ' + str(self.followers) + ' - ' + str(self.followings)

class UserSocialProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.PositiveSmallIntegerField(choices=SOCIAL_PROFILE_PLATFORMS, default=4)
    url = models.URLField()

    class Meta:
        unique_together = [
            # A user can only have 1 profile per platform
            ('user', 'platform')
        ]
        db_table = 'user_social_profile'
        verbose_name_plural = "User Social Profiles"
        verbose_name = "User Social Profile"

    def __str__(self):
        return str(self.user.username) + ' - ' + str(self.platform)


class Ratings(models.Model):
    ratings = models.CharField(max_length=256, choices=RATING_TYPE, default='0')
    username = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        verbose_name_plural = "ratings"
        verbose_name = "ratings"

    def __str__(self):
        return self.ratings


class KarmaPoints(models.Model):
    karma_points = models.IntegerField()

    class Meta:
        verbose_name_plural = "karma_points"
        verbose_name = "karma_points"

    def __int__(self):
        return self.karma_points