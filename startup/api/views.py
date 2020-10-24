from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from startup.models import Startup
from startup.api.serializers import StartupSerializer

@api_view(['GET',])
def api_detail_startup_view(request, slug):
    try:
        startup = get_object_or_404(Startup, pk=slug)
    except Startup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StartupSerializer(startup)
        return Response(serializer.data)


@api_view(['PUT',])
def api_update_startup_view(request, slug):
    try:
        startup = get_object_or_404(Startup, pk=slug)
    except Startup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == "PUT":
        serializer = StartupSerializer(startup, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update sucessful"
            return Response(data=data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE',])
def api_delete_startup_view(request, slug):
    try:
        startup = get_object_or_404(Startup, pk=slug)
    except Startup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == "DELETE":
        operation = startup.delete()
        data = {}
        if operation:
            data['success'] = "delete successful"
        else:
            data['failure'] = "delete failed!"
        return Response(data=data)




@api_view(['POST',])
def api_create_startup_view(request):

    startup = Startup()
    if request.method == "POST":
        serializer = StartupSerializer(startup, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


