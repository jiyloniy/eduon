from api.v1.views.authview import RegisterView, Login
from api.v1.views.auth2 import SocialLoginView
from rest_framework.routers import DefaultRouter
from api.v1.views.videoview import VideoViewSet, CourseViewSet, LessonViewSet

router = DefaultRouter()
router.register(prefix="courses", viewset=CourseViewSet)
router.register(r"lessons", LessonViewSet)
router = DefaultRouter()
router.register(r'videos', VideoViewSet, basename='video')
from django.urls import path, include

urlpatterns = [
    # path("register/", RegisterView.as_view(), name="register"),
    # path("login/", Login.as_view(), name="login"),
    # path("auth/", include("drf_social_oauth2.urls", namespace="drf")),
    path("auth/login/", SocialLoginView.as_view(), name="social_login"),
    path("", include(router.urls)),
]
