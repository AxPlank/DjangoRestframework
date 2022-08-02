from django.urls import path
# from restFrameworkTest.views.views_APIViews import *
# from restFrameworkTest.views.views_Mixins import *
from restFrameworkTest.views.views_Generic import *

urlpatterns = [
    path('', FootballPlayerList.as_view(), name='players_list'),
    path('<int:pk>', FootballPlayerDetail.as_view(), name='player'),
]