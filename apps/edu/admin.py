from django.contrib import admin
from apps.edu.models import Course, Lesson, Video

# Register your models here.

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Video)
