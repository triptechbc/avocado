from app.contrib.api.viewsets import InstructorOrReadOnlyModelViewSet
from app.experiment.models import Attachment, Experiment, Part, Question

from .serializers import (AttachmentSerializer, ExperimentSerializer,
                          PartSerializer, QuestionSerializer)


class ExperimentViewSet(InstructorOrReadOnlyModelViewSet):
    serializer_class = ExperimentSerializer
    queryset = Experiment.objects.all()


class PartViewSet(InstructorOrReadOnlyModelViewSet):
    serializer_class = PartSerializer
    queryset = Part.objects.all()


class AttachmentViewSet(InstructorOrReadOnlyModelViewSet):
    serializer_class = AttachmentSerializer
    queryset = Attachment.objects.all()


class QuestionViewSet(InstructorOrReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
