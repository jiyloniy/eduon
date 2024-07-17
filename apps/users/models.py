from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class User(AbstractUser):
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["user_type"]
    profile_picture = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return self.username



class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name



class Permission(models.Model):
    name =  models.CharField(max_length=100, unique=True)
    codename = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ManyToManyField(Permission)

    def __str__(self) -> str:
        return f"{self.role.name} - {self.permission.name}"
    
class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.role.name}"
    
    class Meta:
        unique_together = ('user', 'role')




