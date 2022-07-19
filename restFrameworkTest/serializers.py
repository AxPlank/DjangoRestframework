from rest_framework import serializers
from .models import *

class FootballPlayerSerializers(serializers.ModelSerializer):
    class Meta:
        model = FootballPlayer
        fields = ('name', 'team', 'position')

class FootballPlayerDetailSerializers(serializers.ModelSerializer):

    name = serializers.CharField(max_length=255)
    height = serializers.FloatField()
    weight = serializers.FloatField()
    team = serializers.CharField(max_length=255)
    position = serializers.CharField(max_length=255)
    uniform_number = serializers.IntegerField()
    profile_img = serializers.ImageField(use_url=True)



    class Meta:
        model = FootballPlayer
        fields = "__all__"