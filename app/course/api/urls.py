# coding: utf-8
from rest_framework import routers

from .views import CourseViewSet

app_name = 'course'

router = routers.SimpleRouter()
router.register(r'', CourseViewSet)
urlpatterns = router.urls
