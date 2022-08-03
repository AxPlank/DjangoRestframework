# app
from restFrameworkTest.serializers import *
# Viewset
from rest_framework.viewsets import ModelViewSet

"""
Written Using Viewset
"""
class FootballPlayerViewset(ModelViewSet):
    queryset = FootballPlayer.objects.all()
    serializer_class = FootballPlayerSerializers