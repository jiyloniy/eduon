from rest_framework import serializers
from apps.edu.models import Course, Lesson, Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            "id",
            "title",
            "kinescope_id",
            "created_at",
            "play_link",
            "embed_link",
            "description",
        ]


class LessonSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ["id", "title", "order", "description", "videos"]


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    instructor = serializers.ReadOnlyField(source="instructor.username")

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "instructor",
            "created_at",
            "updated_at",
            "price",
            "lessons",
        ]


# views.p
