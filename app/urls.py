# coding: utf-8
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

admin.autodiscover()

handler404 = 'app.error_handlers.views.handler404'
handler500 = 'app.error_handlers.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('app.api.urls', namespace='api')),

    path('robots.txt', lambda r: HttpResponse('User-agent: *\nDisallow: /', content_type='text/plain')),
]
