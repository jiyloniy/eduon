from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.edu.models import Course, Lesson, Video
from api.v1.serializers.courseserializers import (
    CourseSerializer,
    LessonSerializer,
    VideoSerializer,
)
from api.v1.utilits.kinoscope import upload_video_to_kinescope
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.edu.models import Course, Lesson, Video
from api.v1.serializers.courseserializers import VideoSerializer
from api.v1.utilits.kinoscope import upload_video_to_kinescope, delete_video
import os
import logging

logger = logging.getLogger(__name__)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=["post"])
    def upload(self, request):
        course_id = request.data.get("course_id")
        lesson_id = request.data.get("lesson_id")
        title = request.data.get("title")
        video_file = request.FILES.get("video_file")
        description = request.data.get("description")
        print(request.FILES.get)
        if not all([course_id, lesson_id, title, video_file]):
            return Response(
                {"error": "Missing required data"}, status=status.HTTP_400_BAD_REQUEST
            )

        course = get_object_or_404(Course, id=course_id, instructor=request.user)
        lesson = get_object_or_404(Lesson, id=lesson_id, course=course)

        temp_file_path = "temp_video.mp4"
        try:
            # Save video file temporarily
            with open(temp_file_path, "wb+") as destination:
                for chunk in video_file.chunks():
                    destination.write(chunk)
            print(1)
            # Upload to Kinescope

            kinescope_response = upload_video_to_kinescope(
                file_path=temp_file_path,
                title=title,
                filename=video_file.name,
                description="Video description",
            )
            print(2)
            if not isinstance(kinescope_response, dict):
                raise ValueError("Invalid response from Kinescope API")

            # Create Video object
            print(kinescope_response)
            kindscope_id = kinescope_response["data"]["id"]
            print(kindscope_id)
            play_link = kinescope_response["data"]["play_link"]
            embed_link = kinescope_response["data"]["embed_link"]
            description = kinescope_response["data"]["description"]
            try:
                video = Video.objects.create(
                    lesson=lesson,
                    title=title,
                    kinescope_id=kindscope_id,
                    play_link=play_link,
                    embed_link=embed_link,
                    description=description,
                )
            except Exception as e:
                delete_video(kindscope_id)
                print(e)
                print(11111111111111111111111111111111111)
                return Response(
                    {"error": "Failed to create video object"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            print(3)
            serializer = VideoSerializer(video)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)

            logger.error(f"Error uploading video: {str(e)}")
            return Response(
                {"error": "Failed to upload video"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        finally:
            # Clean up temporary file
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)
