from rest_framework import serializers

from app.metadata.models import MeasurementUnit, Metadata


class MeasurementUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementUnit
        fields = (
            'name',
            'type',
        )


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = (
            'unit',
            'name',
        )
