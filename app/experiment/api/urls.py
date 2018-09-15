# coding: utf-8
from rest_framework import routers

from .views import (AttachmentViewSet, ExperimentViewSet, PartViewSet,
                    QuestionViewSet)

app_name = 'experiment'

router = routers.SimpleRouter()
router.register(r'parts', PartViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'attachments', AttachmentViewSet)
router.register(r'', ExperimentViewSet)
urlpatterns = router.urls
