from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from .user_profile import UserProfile


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        is_staff = kwargs.pop("is_staff", False)
        is_superuser = kwargs.pop("is_superuser", False)
        is_active = kwargs.pop("is_active", False)

        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            password=password,
            **kwargs
        )
        user.save(using=self._db)

        profile = UserProfile(user=user)
        profile.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email,
            password,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_readonly = models.BooleanField(default=False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(null=False, max_length=255)
    reset_password_token = models.CharField(unique=True, max_length=255, null=True, blank=True)
    reset_password_sent_at = models.DateTimeField(null=True, blank=True)
    remember_created_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)
    confirmation_token = models.CharField(max_length=255, null=True, blank=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    confirmation_sent_at = models.DateTimeField(null=True, blank=True)
    unconfirmed_email = models.EmailField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["reset_password_token"]),
        ]
        app_label = "acc"
        db_table = "User"

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
