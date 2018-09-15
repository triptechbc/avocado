from django.db import models

from app.contrib.models import TimestampedModel


class Experiment(TimestampedModel):
    course = models.ForeignKey('course.Course', related_name='experiments', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date_created',)


class Question(TimestampedModel):
    experiment = models.ForeignKey(Experiment, related_name='questions', on_delete=models.PROTECT)
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('-date_created',)


class Attachment(TimestampedModel):
    experiment = models.ForeignKey(Experiment, related_name='attachments', on_delete=models.PROTECT)
    file = models.FileField(upload_to='data/experiments/attachments/%Y/%m/%d/')

    def __str__(self):
        return self.file.name

    class Meta:
        ordering = ('-date_created',)


class Part(TimestampedModel):
    experiment = models.ForeignKey(Experiment, related_name='parts', on_delete=models.PROTECT)
    procedure = models.TextField()
    metadata = models.ManyToManyField('metadata.Metadata', related_name='parts')
    equipment = models.ManyToManyField('equipment.Equipment', related_name='parts')

    def __str__(self):
        return self.procedure

    class Meta:
        ordering = ('-date_created',)
