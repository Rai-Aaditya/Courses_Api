from django.db import models

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)  # Use AutoField for a unique ID
    title = models.CharField(max_length=255, unique=True)  # Ensure course title is unique
    description = models.TextField()

    def __str__(self):
        return self.title

class CourseDelivery(models.Model):
    year = models.IntegerField()
    semester = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Foreign key

    class Meta:
        unique_together = (('year', 'semester', 'course'),)  # Ensure uniqueness of year, semester, and course combination

    def __str__(self):
        return f"{self.course.title} - {self.year} Semester {self.semester}"
