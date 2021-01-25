from django.db import models
from user.models import User

from ckeditor.fields import RichTextField

CONTENT_TYPE = (('Blog', 'Blog'), ('Itinerary', 'Itinerary'), ('Vlog', 'Vlog'), ('Random', 'Random'))
ITINERARY_TYPE = (('Budget','Budget Friendly'),('Exotic','Exotic'),('Solo','Solo'),('Group','Group'))

class Transport(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    transport_type = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "transport"
        verbose_name = "transport"

    def __str__(self):
        return self.transport_type

class Activities(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    activity_type = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "activities"
        verbose_name = "activities"

    def __str__(self):
        return self.activity_type



class Location(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    location_name = models.CharField(max_length=100)
    location_latitude = models.FloatField(null=True)
    location_longitude = models.FloatField(null=True)
    location_country = models.CharField(max_length=100,null=True)
    location_currency = models.CharField(max_length=100,null=True)
    location_transports = models.ManyToManyField(Transport, related_name="transport_available")
    location_activities = models.ManyToManyField(Activities, related_name="activity_available")

    class Meta:
        verbose_name_plural = "location"
        verbose_name = "location"

    def __str__(self):
        return self.location_name


class travel_log_data(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    user_name = models.ManyToManyField(
                User,related_name='Profile',verbose_name='User',)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='Location',null=True)
    content_type = models.CharField(max_length=256, choices=CONTENT_TYPE, default='Itinerary')
    description = RichTextField(null=True, blank=True, verbose_name='Description')
    itinerary_type = models.CharField(max_length=256, choices=ITINERARY_TYPE, default='Budget')
    upvotes = models.IntegerField(null=True, help_text='No. of upvotes')
    images = models.ImageField(upload_to='images/', null=True)
    days = models.IntegerField(null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    service_cost = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    class Meta:
        verbose_name_plural = "travel_log_data"
        verbose_name = "travel_log_data"

    def __str__(self):
        return str(self.location) + ' - ' + str(self.content_type)

class Reviews(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    travel_id = models.ForeignKey(travel_log_data, on_delete=models.CASCADE)
    reviewer_username = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=265,default='',null=False)

    class Meta:
        verbose_name_plural = "reviews"
        verbose_name = "reviews"