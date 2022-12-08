from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Video
from .serializers import *

@api_view(['GET', 'POST'])
def videos(request):
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many = True)
        return(Response({'data': serializer.data}))
    elif request.method == 'POST':
        video = Video()
        video.save()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def like_video(request, post_id):
   if request.method == 'GET':
    try:
        video = Video.objects.get(id = post_id)
    except:
        return Response(status = status.HTTP_400_BAD_REQUEST)

    setattr(video, 'likesCount', video.likesCount + 1)
    video.save()
    return Response(video.likesCount, status.HTTP_200_OK)