# coding: utf-8
from django.contrib.auth.backends import ModelBackend

from app.users.models import User


class UserAuthBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        try:
            user = User.objects.get(username=kwargs.get('username'))
            if user.check_password(kwargs.get('password')):
                return user
        except User.DoesNotExist:
            return

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return
