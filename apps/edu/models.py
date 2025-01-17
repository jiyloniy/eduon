from django.db import models
from apps.users.models import User


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="courses"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_free = models.BooleanField(default=False)
    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    order = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Video(models.Model):
    lesson = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=200)
    kinescope_id = models.CharField(max_length=100)
    # duration = models.IntegerField(help_text="Duration in seconds",)
    play_link = models.URLField()
    embed_link = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





# models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as gis_models


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    location = gis_models.PointField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name