from api.v1.views.auth import SocialLoginView,Login


from django.urls import path, include

urlpatterns = [
    path("auth/login/", SocialLoginView.as_view(), name="social_login"),
    path("auth/auth/", Login.as_view(), name="loginform"),
 
]
