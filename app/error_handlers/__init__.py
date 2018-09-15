# coding: utf-8
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    code = getattr(response, 'status_code', HTTP_500_INTERNAL_SERVER_ERROR)
    errors = getattr(response, 'data', {'non_field_errors': str(exc)})
    return Response({
        'code': code,
        'errors': errors
    }, status=code)
