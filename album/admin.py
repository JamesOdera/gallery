from django.contrib import admin
from .models import Editor,Article,tags,Category,Location

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)
admin.site.register(Category)
admin.site.register(Location)