from django.contrib import admin
from apps.users.models import User,RolePermission,Role,Permission,UserRole

# Register your models here.

admin.site.register(User)
admin.site.register(RolePermission)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(UserRole)

