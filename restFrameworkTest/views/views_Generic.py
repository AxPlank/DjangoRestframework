# app
from restFrameworkTest.serializers import *
# Mixins
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

"""
Written Using Generic
"""
class FootballPlayerList(ListCreateAPIView):
    queryset = FootballPlayer.objects.all()
    serializer_class = FootballPlayerSerializers

class FootballPlayerDetail(RetrieveUpdateDestroyAPIView):
    queryset = FootballPlayer.objects.all()
    serializer_class = FootballPlayerSerializers
