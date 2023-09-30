# serializers.py
from rest_framework import serializers
from .models import Course, CourseDelivery

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDelivery
        fields = '__all__'


class CustomCourseDeliverySerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title')
    course_year = serializers.IntegerField(source='year')
    course_semester = serializers.IntegerField(source='semester')
    course_id = serializers.IntegerField(source='course.course_id')

    class Meta:
        model = CourseDelivery
        fields = ['course_title', 'course_year', 'course_semester', 'course_id']