from rest_framework import serializers

from app.course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'name',
            'code',
            'year',
            'semester',
            'date_start',
            'date_end',
        )
