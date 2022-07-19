# app
from .serializers import *
# rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import FileUploadParser
# django
from django.shortcuts import get_object_or_404

# Create your views here.

# Collection
class FootballPlayerList(APIView):

    def get(self, request):
        # GET
        queryset = FootballPlayer.objects.all()
        serializer = FootballPlayerSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        # POST
        serializer = FootballPlayerDetailSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FootballPlayerDetail(APIView):
    def get(self, request, player_id):
        # GET
        queryset = get_object_or_404(FootballPlayer, id=player_id)
        serializer = FootballPlayerDetailSerializers(queryset)
        return Response(serializer.data)

    def put(self, request, player_id):
        # PUT
        queryset = FootballPlayer.objects.get(id=player_id)
        serializer = FootballPlayerDetailSerializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, player_id):
        # DELETE
        queryset = FootballPlayer.objects.get(id=player_id)
        queryset.delete()
        return Response("Delete completed", status=status.HTTP_200_OK)