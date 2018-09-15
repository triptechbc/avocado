from django.db import models


class TimestampedModel(models.Model):
    """
    Abstract common model for all models in application, contain data about entry creation and updates.
    """
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
