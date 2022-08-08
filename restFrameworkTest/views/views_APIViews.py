# app
from restFrameworkTest.serializers import *
# rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# django
from django.shortcuts import get_object_or_404

"""
Written Using APIView
"""
class FootballPlayerList(APIView):

    def get(self, request):
        # GET
        queryset = FootballPlayer.objects.all()
        serializer = FootballPlayerSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        # POST
        serializer = FootballPlayerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FootballPlayerDetail(APIView):
    def get(self, request, pk):
        # GET
        queryset = get_object_or_404(FootballPlayer, id=pk)
        serializer = FootballPlayerSerializers(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        # PUT
        queryset = FootballPlayer.objects.get(id=pk)
        serializer = FootballPlayerSerializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # DELETE
        queryset = FootballPlayer.objects.get(id=pk)
        queryset.delete()
        return Response("Delete completed", status=status.HTTP_200_OK)