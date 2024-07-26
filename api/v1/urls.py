from api.v1.views.auth import SocialLoginView,Login
from api.v1.views.teacherview import TeacherCreateView,TeacherListView,TeacherGetView

# url



from django.urls import path, include

urlpatterns = [
    path("auth/social/login/", SocialLoginView.as_view(), name="social_login"),
    path("auth/login/", Login.as_view(), name="loginform"),
    path("teacher/create/", TeacherCreateView.as_view(), name="teacher_create"),
    path("teacher/list/", TeacherListView.as_view(), name="teacher_list"),
    path("teacher/get/<int:pk>/", TeacherGetView.as_view(), name="teacher_get"),
    
]   
