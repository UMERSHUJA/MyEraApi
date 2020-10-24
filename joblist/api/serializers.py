from rest_framework import serializers
from joblist.models import JobList

class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobList
        fields = ['id', 'job_title', 'description', 'icon','company_name', 'experience', 'job_type', 'destinaion', 'job_link']
