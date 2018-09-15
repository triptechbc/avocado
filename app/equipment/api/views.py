from app.contrib.api.viewsets import AdminOrReadOnlyModelViewSet
from app.equipment.models import Equipment

from .serializers import EquipmentSerializer


class EquipmentViewSet(AdminOrReadOnlyModelViewSet):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()
