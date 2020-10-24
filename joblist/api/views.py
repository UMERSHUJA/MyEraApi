from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from joblist.models import JobList
from joblist.api.serializers import JobListSerializer

@api_view(['GET',])
def api_detail_job_view(request, slug):
    try:
        job = get_object_or_404(JobList, pk=slug)
    except job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StartupSerializer(job)
        return Response(serializer.data)


@api_view(['PUT',])
def api_update_job_view(request, slug):
    try:
        job = get_object_or_404(JobList, pk=slug)
    except JobList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == "PUT":
        serializer = JobListSerializer(job, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update sucessful"
            return Response(data=data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE',])
def api_delete_job_view(request, slug):
    try:
        job = get_object_or_404(JobList, pk=slug)
    except JobList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == "DELETE":
        operation = job.delete()
        data = {}
        if operation:
            data['success'] = "delete successful"
        else:
            data['failure'] = "delete failed!"
        return Response(data=data)




@api_view(['POST',])
def api_create_job_view(request):

    job = JobList()
    if request.method == "POST":
        serializer = JobListSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


