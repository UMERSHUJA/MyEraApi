from django.contrib import admin
from . import models


class StartupAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'is_sponsered', 'published')
    list_display_links = ('id', 'product_name')
    list_editable = ('published', )
    search_fields = ('product_name', 'price')
    list_per_page = 25



admin.site.register(models.Startup, StartupAdmin)
