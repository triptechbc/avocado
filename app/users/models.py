# coding: utf-8
import operator
from functools import reduce

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models import Q


class UserManager(BaseUserManager):
    def create_superuser(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        admin_role, created = UserRole.objects.get_or_create(name=UserRole.ADMIN)
        user.roles.add(admin_role)
        return user


class UserRole(models.Model):
    ADMIN = 'ADMIN'
    INSTRUCTOR = 'INSTRUCTOR'

    name = models.CharField(max_length=255, choices=(
        (ADMIN, ADMIN),
        (INSTRUCTOR, INSTRUCTOR),
    ))

    def __str__(self):
        return self.name


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)

    roles = models.ManyToManyField(UserRole)

    objects = UserManager()

    def __str__(self):
        return self.get_full_name()

    def has_role(self, role):
        return self.roles.filter(name=role).exists()

    def has_roles(self, roles):
        # Checks if user has at least one role from roles.
        q = [Q(name=role) for role in roles]
        return self.roles.filter(reduce(operator.or_, q)).exists()

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.username

    def get_short_name(self):
        if self.first_name:
            return self.first_name
        return self.username

    def has_module_perms(self, *args, **kwargs):
        return self.has_role(role=UserRole.ADMIN)

    def has_perm(self, *args, **kwargs):
        return self.has_role(role=UserRole.ADMIN)

    def is_staff(self):
        return self.has_role(role=UserRole.ADMIN)

    def is_superuser(self):
        return self.has_role(role=UserRole.ADMIN)
