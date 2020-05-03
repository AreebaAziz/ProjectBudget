from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy as _
from MyUser.admin import ADMIN_MODELS as MyUser_admin_models

class ProjectAdminSite(AdminSite):
	site_title = _("My Project")
	site_header = _("My Project - Admin")

def register_admin_models(admin_site, admin_models):
	for models in admin_models:
		admin_site.register(*models)

admin_site = ProjectAdminSite()
register_admin_models(admin_site, MyUser_admin_models)