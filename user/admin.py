from django.contrib import admin
from .models import *

from easy_select2 import select2_modelform
from django.contrib.auth.models import User

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin


@admin.register(Username)
class UsernameAdmin(admin.ModelAdmin):
    fields=[
        ('username'),
        ('user_type'),
        ('followers'),
        ('followings'),
    ]
    '''list_display = ('user_id','user_name','followers','followings')'''


@admin.register(UserId)
class UserIdAdmin(admin.ModelAdmin):
    fields=[
        ('user_id')
    ]
    pass

@admin.register(Ratings)
class RatingsAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fields=[
        ('ratings')
    ]


@admin.register(KarmaPoints)
class KPointsAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fields=[
        ('karma_points'),
    ]
    '''list_display = ('karma_points')'''
