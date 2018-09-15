from django.core.exceptions import FieldDoesNotExist

from rest_framework import permissions, viewsets

from .permissions import IsAdminUser, IsInstructorUser


class HasRoleOrReadOnlyModelViewSet(viewsets.ModelViewSet):
    destructive_actions = ('update', 'create', 'delete')
    required_permission = None


    def perform_create(self, serializer):
        try:
            serializer.save(created_by=self.request.user)
        except TypeError:
            serializer.save()

    def get_permissions(self):
        if self.action in self.destructive_actions:
            permission_classes = [self.required_permission]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class AdminOrReadOnlyModelViewSet(HasRoleOrReadOnlyModelViewSet):
    required_permission = IsAdminUser



class InstructorOrReadOnlyModelViewSet(HasRoleOrReadOnlyModelViewSet):
    required_permission = IsInstructorUser
