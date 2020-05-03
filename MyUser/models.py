from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import MyUserManager

class MyUser(AbstractUser):

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ['password']

	email = models.EmailField(_('email address'), unique=True)
	username = models.CharField(max_length=255, null=True, blank=True, unique=False)

	objects = MyUserManager()

	class Meta:
		app_label = "MyUser"

	def __str__(self):
		return self.first_name + " " + self.last_name