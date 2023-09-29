from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Course, CourseDelivery
from .serializers import CourseSerializer, CourseDeliverySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class CourseInfoView(APIView):
    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            course_data = {
                'title': course.title,
                'course_id': course.course_id,
            }
            return Response(course_data)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=404)


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class NewInstanceCreateView(generics.CreateAPIView):
    queryset = CourseDelivery.objects.all()
    serializer_class = CourseDeliverySerializer

class InstanceListView(generics.ListAPIView):
    queryset = CourseDelivery.objects.all()
    serializer_class = CourseDeliverySerializer

class InstanceListByYearSemesterView(generics.ListAPIView):
    serializer_class = CourseDeliverySerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseDelivery.objects.filter(year=year, semester=semester)

class InstanceDetailView(generics.RetrieveDestroyAPIView):
    queryset = CourseDelivery.objects.all()
    serializer_class = CourseDeliverySerializer

class InstanceDeleteView(generics.DestroyAPIView):
    queryset = CourseDelivery.objects.all()
    serializer_class = CourseDeliverySerializer