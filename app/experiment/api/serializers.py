from rest_framework import serializers

from app.experiment.models import Attachment, Experiment, Part, Question


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = (
            'course',
            'name',
            'description',
            'deadline',
        )


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = (
            'experiment',
            'procedure'
        )


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = (
            'experiment',
            'file'
        )


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'experiment',
            'text'
        )
