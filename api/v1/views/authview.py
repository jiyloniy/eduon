from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework.exceptions import (
    AuthenticationFailed,
    NotAuthenticated,
    ValidationError,
)
from api.v1.serializers.authserializer import LoginSerializers
class Login(APIView):
    serializer_class = LoginSerializers

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        user_type = 'admin' if user.user_type==1 else 'user' if user.user_type ==2 else 'student' if user.user_type==3 else 'teacher' if user_type == 4 else 'manager' 
        refresh = RefreshToken.for_user(user)
        refresh["test"] = "test"
        return Response({"refresh": str(refresh), "access": str(refresh.access_token)})
