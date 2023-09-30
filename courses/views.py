# views.py
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Course, CourseDelivery
from .serializers import CourseSerializer, CourseDeliverySerializer, CustomCourseDeliverySerializer
from django.http import Http404

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
    serializer_class = CustomCourseDeliverySerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseDelivery.objects.filter(year=year, semester=semester)

class InstanceDetailView(generics.RetrieveDestroyAPIView):
    queryset = CourseDelivery.objects.all()
    serializer_class = CourseDeliverySerializer


class CourseDeliveryDeleteView(generics.DestroyAPIView):
    serializer_class = CustomCourseDeliverySerializer

    def get_object(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        course_id = self.kwargs['pk']

        try:
            return CourseDelivery.objects.get(year=year, semester=semester, course_id=course_id)
        except CourseDelivery.DoesNotExist:
            raise Http404

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)