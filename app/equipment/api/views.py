from app.contrib.api.viewsets import AdminOrReadOnlyModelViewSet
from app.equipment.models import Equipment

from .serializers import EquipmentSerializer


class EquipmentViewSet(AdminOrReadOnlyModelViewSet):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()

    def perform_create(self, serializer):
        self.set_created_by(created_object=serializer.save())
