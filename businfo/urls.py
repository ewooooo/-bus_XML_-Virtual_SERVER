from django.urls import path
from .views import *

urlpatterns = [
    path('busrouteservice/info', busrouteservice),
    path('busarrivalservice/station', busarrivalservice),
]