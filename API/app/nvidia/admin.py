from django.contrib import admin
from .models import *
from mapwidgets.widgets import GooglePointFieldInlineWidget
import requests, json



@admin.register(ImageSegmentation)
class ImageSegmentationAdmin(admin.ModelAdmin):
    list_display = ('uuid','name','created_at', 'updated_at', 'active' )
    list_filter = ('verified', 'active')
    search_fields = ('name',)
    date_hierarchy = 'created_at'
