from django.contrib import admin
from .models import *

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'location', 'category',)
    list_filter = ('pub_date',)
    search_fields = ('title', 'category', 'location')

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image, ImageAdmin)