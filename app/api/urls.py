# coding: utf-8
from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('users/', include('app.users.api.urls', namespace='users')),
    path('equipment/', include('app.equipment.api.urls', namespace='equipment')),
    path('metadata/', include('app.metadata.api.urls', namespace='metadata')),
    path('course/', include('app.course.api.urls', namespace='course')),
    path('experiment/', include('app.experiment.api.urls', namespace='experiment')),
]
