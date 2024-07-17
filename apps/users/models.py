from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Admin'),
        (2, 'User'),
        (3, 'Student'),
        (4, 'Teacher'),
        (5, 'Manager'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=2)
    profile_picture = models.URLField(max_length=500, blank=True, null=True)

# class NewUserRole(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.user.username} - {self.role}"``