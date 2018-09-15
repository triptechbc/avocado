from app.contrib.api.viewsets import AdminOrReadOnlyModelViewSet
from app.course.models import Course

from .serializers import CourseSerializer


class CourseViewSet(AdminOrReadOnlyModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

