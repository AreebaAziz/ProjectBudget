from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not password:
            raise ValueError(_('The Password must be set'))
        email = self.normalize_email(email)
        user = get_user_model()(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        return self.create_user( 
            email=email, 
            password=password, 
            is_staff=True, 
            is_superuser=True,
            is_active=True,
            **extra_fields
        )