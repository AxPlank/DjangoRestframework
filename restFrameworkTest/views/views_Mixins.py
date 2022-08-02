# app
from restFrameworkTest.serializers import *
# Mixins
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin, UpdateModelMixin

"""
Written Using Mixins
"""
class FootballPlayerList(CreateModelMixin,
                         ListModelMixin,
                         GenericAPIView):

    queryset = FootballPlayer.objects.all()
    serializer_class = FootballPlayerSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class FootballPlayerDetail(RetrieveModelMixin,
                           UpdateModelMixin,
                           DestroyModelMixin,
                           GenericAPIView):

    queryset = FootballPlayer.objects.all()
    serializer_class = FootballPlayerSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)