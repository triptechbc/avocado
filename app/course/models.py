from django.db import models

from app.contrib.models import TimestampedModel


class Course(TimestampedModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=64)
    year = models.PositiveIntegerField()
    semester = models.CharField(max_length=16)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    users = models.ManyToManyField('users.User', related_name='assigned_courses')
    created_by = models.ForeignKey('users.User', related_name='created_courses', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} ({self.code})'
