
from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, is_shop_owner, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            is_shop_owner=is_shop_owner,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, is_shop_owner, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            is_shop_owner=is_shop_owner,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

