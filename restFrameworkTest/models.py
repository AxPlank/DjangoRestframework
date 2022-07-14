from django.db import models

# Create your models here.

class FootballPlayer(models.Model):
    name = models.CharField(max_length=255)
    height = models.FloatField()
    weight = models.FloatField()
    team = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    uniform_number = models.IntegerField()
    profile_img = models.ImageField(upload_to=f'media/')

    def __str__(self):
        return f'{self.team} - {self.name}'