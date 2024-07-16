from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class User(AbstractUser):
    TYPE = (
        (1, "student"),
        (2, "admin"),
        (3, "teacher"),
    )
    user_type = models.PositiveSmallIntegerField(default=1)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["user_type"]
    profile_picture = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return self.username


class UserMixin(models.Model):
    name = models.CharField(_("Ism"), max_length=50)
    surname = models.CharField(_("Familiya"), max_length=50)
    age = models.PositiveIntegerField(_("Yosh"))
    address = models.CharField(_("Manzil"), max_length=50)

    class Meta:
        abstract = True
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Student(UserMixin):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student",
        related_query_name="student",
    )

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})


class Admin(UserMixin):

    user = models.OneToOneField(
        "User",
        verbose_name=_(""),
        on_delete=models.CASCADE,
        related_name="admin",
        related_query_name="admin",
    )

    class Meta:
        verbose_name = _("Admin")
        verbose_name_plural = _("Admins")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Admin_detail", kwargs={"pk": self.pk})


class Teacher(UserMixin):
    user = models.OneToOneField(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="teacher",
        related_query_name="teacher",
    )

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Teacher_detail", kwargs={"pk": self.pk})


from django.template import Context, Template
