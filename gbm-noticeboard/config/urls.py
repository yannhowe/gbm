from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

# django-cruds-adminlte
from django.apps import apps
from cruds_adminlte.urls import crud_for_model

urlpatterns = [
    path('admin/', admin.site.urls),
    url('noticeboard/', include('project.noticeboard.urls')),
    url(r'^accounts/', include('allauth.urls')),
]

# django-cruds-adminlte
urlpatterns += crud_for_model(apps.get_model('noticeboard', 'Missionary'))
urlpatterns += crud_for_model(apps.get_model('noticeboard', 'Update'))
