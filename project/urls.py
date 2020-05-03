"""project_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from MyUser.views import login, signup
from .admin import admin_site
from .views import index, base_dashboard

urlpatterns = [
    path('admin/', admin_site.urls),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('', index, name='index'),
    path('in/', base_dashboard, name='base_dashboard'),
    path('user/', include('MyUser.urls')),
]
