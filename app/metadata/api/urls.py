# coding: utf-8
from rest_framework import routers

from .views import MeasurementUnitViewSet, MetadataViewSet

app_name = 'metadata'

router = routers.SimpleRouter()
router.register(r'units', MeasurementUnitViewSet)
router.register(r'', MetadataViewSet)
urlpatterns = router.urls
