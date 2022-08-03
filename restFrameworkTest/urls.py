from django.urls import path, include
# views.py
# from restFrameworkTest.views.views_APIViews import *
# from restFrameworkTest.views.views_Mixins import *
# from restFrameworkTest.views.views_Generic import *
from restFrameworkTest.views.views_Viewset import *
# Viewset
from rest_framework.routers import DefaultRouter

"""
as_view()
"""
footballplayer_list = FootballPlayerViewset.as_view(
    {'get': 'list',
     'post': 'create'}
)

footballpalyer_detail = FootballPlayerViewset.as_view(
    {'get': 'retrieve',
     'put': 'update',
     'delete': 'destroy'}
)

"""
router
"""
# r = DefaultRouter()
# r.register('', FootballPlayerViewset)

urlpatterns = [
    # # APIView, Mixins, Generic
    # path('', FootballPlayerList.as_view(), name='players_list'),
    # path('<int:pk>', FootballPlayerDetail.as_view(), name='player'),
    #
    # # Viewset - as_view()
    path('', footballplayer_list),
    path('<int:pk>/', footballpalyer_detail),

    # # viewset - router
    # path('', include(r.urls)),
]