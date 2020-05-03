from django.urls import path

from .views import logout

app_name = "MyUser"

urlpatterns = [
	path('logout', logout, name='logout'),
]