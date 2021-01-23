from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

RATING_TYPE = (('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'))

class Username(models.Model):
    username = models.CharField(max_length = 100)
    user_type = models.CharField(max_length=100)
    followers = models.IntegerField()
    followings = models.IntegerField()

    class Meta:
        verbose_name_plural = "username"
        verbose_name = "username"

    def __str__(self):
        return self.username_type

class UserId(models.Model):
    user_id = models.IntegerField()

    class Meta:
        verbose_name_plural = "userid"
        verbose_name = "userid"

    def __str__(self):
        return self.user_type



class Ratings(models.Model):
    ratings = models.CharField(max_length=256, choices=RATING_TYPE, default='0')

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