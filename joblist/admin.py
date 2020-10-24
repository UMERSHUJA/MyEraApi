from django.contrib import admin
from . import models


class JoblistAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'published')
    list_display_links = ('id', 'job_title')
    search_fields = ('job_title', 'job_type')
    list_editable = ('published', )
    list_per_page = 25


admin.site.register(models.JobList, JoblistAdmin)
