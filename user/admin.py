from django.contrib import admin
from .models import *

from easy_select2 import select2_modelform

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, ExportActionMixin,admin.ModelAdmin):
    pass

@admin.register(UserSocialProfile)
class UserSocialProfileAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    pass

@admin.register(Ratings)
class RatingsAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fields=[
        ('username'),
        ('ratings')
    ]

@admin.register(Follow)
class FollowAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    pass

@admin.register(KarmaPoints)
class KPointsAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fields=[
        ('karma_points'),
    ]
    '''list_display = ('karma_points')'''
