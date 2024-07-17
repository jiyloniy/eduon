from apps.users.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "user_type", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise AuthenticationFailed('Invalid username or password')
            if not user.is_active:
                raise AuthenticationFailed('User account is disabled')
        else:
            raise AuthenticationFailed('Must include password and username')
        
        attrs['user'] = user
        return attrs
        
