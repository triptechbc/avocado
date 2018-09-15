# coding: utf-8
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from .views import CurrentUserAPIView

app_name = 'users'

urlpatterns = [
    path('current_user/', CurrentUserAPIView.as_view(), name='current_user'),
    path('authenticate/', ObtainAuthToken.as_view(), name='authenticate'),
]
