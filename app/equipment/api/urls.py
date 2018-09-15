# coding: utf-8
from rest_framework import routers

from .views import EquipmentViewSet

app_name = 'equipment'

router = routers.SimpleRouter()
router.register(r'', EquipmentViewSet)
urlpatterns = router.urls
