from rest_framework.permissions import BasePermission

from app.users.models import UserRole


class BaseAppPermission(BasePermission):
    possible_roles = []

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.has_roles(roles=self.possible_roles)


class IsAdminUser(BaseAppPermission):
    possible_roles = [UserRole.ADMIN]


class IsInstructorUser(BaseAppPermission):
    possible_roles = [UserRole.ADMIN, UserRole.INSTRUCTOR]
