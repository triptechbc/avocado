from rest_framework import permissions, viewsets

from .permissions import IsAdminUser, IsInstructorUser


class HasRoleOrReadOnlyModelViewSet(viewsets.ModelViewSet):
    destructive_actions = ('update', 'create', 'delete')
    required_permission = None

    def set_created_by(self, created_object):
        created_object.created_by = self.request.user
        created_object.save(update_fields=['created_by'])

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
