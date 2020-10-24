from django.db import models
from datetime import datetime


class JobList(models.Model):
    job_title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='JobList')
    company_name = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    job_type = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    job_link = models.CharField(max_length=100)
    submission_date = models.DateTimeField(default=datetime.now, blank=False)
    published = models.BooleanField(default=False)
    user_id = models.IntegerField(default=0, blank=True)
    def __str__(self):
        return self.job_title

