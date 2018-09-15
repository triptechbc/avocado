from django.db import models

from app.contrib.models import TimestampedModel


class Equipment(TimestampedModel):
    name = models.CharField(max_length=512)
    description = models.TextField()
    metadata = models.ManyToManyField('metadata.Metadata', related_name='equipments')
    created_by = models.ForeignKey('users.User', related_name='equipments', on_delete=models.PROTECT)
