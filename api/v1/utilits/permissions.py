# teacher and admin permissions
from rest_framework.permissions import BasePermission
from apps.users.models import User


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        try:
            user = User.objects.get(id=request.user.id)
            return True if user.user_type == 4 else False
        except User.DoesNotExist:
            return False
    
    def has_object_permission(self, request, view, obj):
        try:
            user = User.objects.get(id=request.user.id)
            return True if user.user_type == 4 and user.id == obj.user.id else False
        except User.DoesNotExist:
            return False
        
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            user = User.objects.get(id=request.user.id)
            return True if user.user_type == 1 else False
        except User.DoesNotExist:
            return False
    
    def has_object_permission(self, request, view, obj):
        try:
            user = User.objects.get(id=request.user.id)
            return True if user.user_type == 1 else False
        except User.DoesNotExist:
            return False
        
    
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        try:
            user = User.objects.get(id=request.user.id)
            return True if user.user_type == 3 else False
        except User.DoesNotExist:
            return False
    
    def has_object_permission(self, request, view, obj):
        try:
            user = User.objects.get(id=request.user.id)
            return True if user.user_type == 3 and user.id == obj.user.id else False
        except User.DoesNotExist:
            return False