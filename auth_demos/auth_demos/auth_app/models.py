from django.contrib.auth import get_user_model, models as auth_models
# Create your models here.

from django.db import models

from auth_demos.auth_app.managers import AppUsersManager
#
# UserModel = get_user_model()

#
# """
# Proxy Model
# """
# class UserWithFullNameProxy(UserModel):
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    USERNAME_FIELD = 'email'
    is_staff = models.BooleanField(
        default=False,
    )

    objects = AppUsersManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
