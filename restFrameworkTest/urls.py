from django.urls import path
from .views import *

urlpatterns = [
    path('', FootballPlayerList.as_view(), name='players_list'),
    path('<int:player_id>', FootballPlayerDetail.as_view(), name='player'),
]