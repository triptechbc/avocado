from app.contrib.api.viewsets import AdminOrReadOnlyModelViewSet
from app.course.models import Course

from .serializers import CourseSerializer


class CourseViewSet(AdminOrReadOnlyModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        self.set_created_by(created_object=serializer.save())
