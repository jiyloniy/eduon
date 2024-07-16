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
from api.v1.serializers.authserializer import RegisterSerializer, LoginSerializers


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serilizer = self.serializer_class(data=request.data)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        login(request, serilizer.instance)
        refresh = RefreshToken.for_user(serilizer.instance)
        return Response({"refresh": str(refresh), "access": str(refresh.access_token)})


class Login(APIView):
    serializer_class = LoginSerializers

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        refresh["test"] = "test"
        return Response({"refresh": str(refresh), "access": str(refresh.access_token)})
