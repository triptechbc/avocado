from app.contrib.api.viewsets import AdminOrReadOnlyModelViewSet
from app.metadata.models import MeasurementUnit, Metadata

from .serializers import MeasurementUnitSerializer, MetadataSerializer


class MeasurementUnitViewSet(AdminOrReadOnlyModelViewSet):
    serializer_class = MeasurementUnitSerializer
    queryset = MeasurementUnit.objects.all()


class MetadataViewSet(AdminOrReadOnlyModelViewSet):
    serializer_class = MetadataSerializer
    queryset = Metadata.objects.all()

    def perform_create(self, serializer):
        self.set_created_by(created_object=serializer.save())
