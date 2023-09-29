from django.db import models

class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)  # Primary key
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class CourseDelivery(models.Model):
    year = models.IntegerField()
    semester = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Foreign key

    def __str__(self):
        return f"{self.course.title} - {self.year} Semester {self.semester}"
