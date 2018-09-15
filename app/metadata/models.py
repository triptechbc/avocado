from django.db import models

from app.contrib.models import TimestampedModel


class MeasurementUnit(TimestampedModel):
    STRING = 'STRING'
    INTEGER = 'INTEGER'
    FLOAT = 'FLOAT'
    DECIMAL = 'DECIMAL'

    UNIT_TYPE_CHOICES = (
        (STRING, STRING),
        (INTEGER, INTEGER),
        (FLOAT, FLOAT),
        (DECIMAL, DECIMAL)
    )

    name = models.CharField(max_length=255)
    type = models.CharField(choices=UNIT_TYPE_CHOICES, max_length=16)

    def __str__(self):
        return self.name


class Metadata(TimestampedModel):
    unit = models.ForeignKey(MeasurementUnit, related_name='metadata', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey('users.User', related_name='metadata', on_delete=models.PROTECT)

    class Meta:
        unique_together = ('unit', 'name')

    def __str__(self):
        return self.name
