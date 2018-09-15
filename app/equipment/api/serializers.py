from rest_framework import serializers

from app.equipment.models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = (
            'name',
            'description',
        )
