from django.urls import path
from . import views

urlpatterns = [
    path('api/courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
    path('api/courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('api/courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course-delete'),
    path('api/instances/add/', views.NewInstanceCreateView.as_view(), name='instance-create'),
    path('api/instances/', views.InstanceListView.as_view(), name='instance-list'),
    path('api/instances/<int:year>/<int:semester>/', views.InstanceListByYearSemesterView.as_view(), name='instance-list-by-year-semester'),
    path('api/instances/<int:year>/<int:semester>/<int:pk>/', views.InstanceDetailView.as_view(), name='instance-detail'),
    path('api/instances/<int:year>/<int:semester>/<int:pk>/delete/', views.InstanceDeleteView.as_view(), name='instance-delete'),
]
