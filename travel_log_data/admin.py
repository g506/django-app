from django.contrib import admin
from .models import *

from easy_select2 import select2_modelform
from django.contrib.auth.models import User

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin


@admin.register(travel_log_data)
class TravelAdmin(admin.ModelAdmin):
    fields=[
        ('travel_id'),
        ('user_name'),
        ('location','content_type'),
        ('description'),
        ('itinerary_type'),('upvotes'),
        ('images'),
        ('days'),
        ('cost','service_cost'),
    ]
    list_display = ('travel_id','location','service_cost','itinerary_type','upvotes')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Transport)
class TransportAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fields=[
        ('transport_type')
    ]

@admin.register(Activities)
class ActivitiesAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fields=[
        ('activity_id'),
        ('activity_type')
    ]
    list_display = ('activity_type','activity_id')

@admin.register(Reviews)
class ReviewsAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fields=[
        ('review_id'),
        ('travel_id'),
        ('reviewer_username'),
    ]
    list_display = ('review_id','travel_id','reviewer_username')