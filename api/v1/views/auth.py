from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from social_django.utils import load_strategy, load_backend
from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, login
from django.contrib.auth import authenticate
from api.v1.serializers.authserializer import LoginSerializers
from rest_framework.views import APIView
User = get_user_model()


class SocialLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        provider = request.data.get("provider")
        code = request.data.get("code")

        if not provider or not code:
            return Response(
                {"error": "Provider va kod talab qilinadi."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        strategy = load_strategy(request)

        try:
            backend = load_backend(strategy=strategy, name=provider, redirect_uri=None)
        except MissingBackend:
            return Response(
                {"error": "Yaroqli provayderga murojaat qiling."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = backend.do_auth(code)
        except AuthTokenError:
            return Response(
                {"error": "Yaroqsiz hisob ma'lumotlari."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except AuthForbidden:
            return Response(
                {"error": "Bu foydalanuvchi faol emas."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if user:
            user_obj, created = User.objects.get_or_create(
                email=user.email,
                defaults={"username": user.email, "user_type": 3},  # student
            )

            # Update profile picture
            if provider == "google-oauth2":
                user_obj.profile_picture = user.social_user.extra_data.get("picture")
            elif provider == "github":
                user_obj.profile_picture = user.social_user.extra_data.get("avatar_url")

            user_obj.save()

            # Authenticate and login the user
            authenticated_user = authenticate(
                request, username=user_obj.username, password=user_obj.password
            )
            if authenticated_user:
                login(request, authenticated_user)

            refresh = RefreshToken.for_user(user_obj)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "username": user_obj.username,
                }
            )
        else:
            return Response(
                {"error": "Autentifikatsiya muvaffaqiyatsiz tugadi."},
                status=status.HTTP_400_BAD_REQUEST,
            )



class Login(APIView):
    serializer_class = LoginSerializers

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user)
        user_type = 'admin' if user.user_type==1 else 'user' if user.user_type ==2 else 'student' if user.user_type==3 else 'teacher' if user_type == 4 else 'manager' 
        refresh = RefreshToken.for_user(user)
        refresh['user_type'] = user_type
        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        })
