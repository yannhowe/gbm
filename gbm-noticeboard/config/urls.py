from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from django.views.generic.base import TemplateView

# django-cruds-adminlte
from django.apps import apps
from cruds_adminlte.urls import crud_for_app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cp/', TemplateView.as_view(template_name='adminlte/home.html')),
    url('', include('project.noticeboard.urls')),
    url('', include('allauth.urls')),
]

# django-cruds-adminlte
urlpatterns += crud_for_app('noticeboard', login_required=True, check_perms=True, cruds_url='cp')
