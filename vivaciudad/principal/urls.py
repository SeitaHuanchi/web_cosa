from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('eventos/', eventos, name='eventos'),
]
