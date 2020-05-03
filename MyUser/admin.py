from django.contrib.admin import ModelAdmin
from .models import MyUser

class MyUserAdmin(ModelAdmin):
	list_display = ('first_name', 'last_name', 'email', 'last_login', 'is_active', 'is_staff')
	list_display_links = ('first_name', 'last_name', 'email')
	fields = ('email', 'password', 'first_name', 'last_name', 'is_staff', 'is_superuser')

# admin.site.register(MyUser, MyUserAdmin)

ADMIN_MODELS = [(MyUser, MyUserAdmin)]