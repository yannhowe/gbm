from django.contrib import admin
from .models import Missionary, Update

# django Import/Export Stuff
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportMixin


# django-import-export stuff
class MissionaryResource(resources.ModelResource):
    class Meta:
        model = Missionary
        fields = ('id', 'friendly_name', 'email', 'country','profile', 'profile_picture', 'upcoming', 'prayer')

class MissionaryAdmin(ImportExportModelAdmin, ExportMixin):
    resource_class = MissionaryResource

admin.site.register(Missionary, MissionaryAdmin)

class UpdateResource(resources.ModelResource):
    class Meta:
        model = Update

class UpdateAdmin(ImportExportModelAdmin, ExportMixin):
    resource_class = UpdateResource

admin.site.register(Update, UpdateAdmin)
