from api.v1.views.auth2 import SocialLoginView


from django.urls import path, include

urlpatterns = [
    path("auth/login/", SocialLoginView.as_view(), name="social_login"),
 
]
