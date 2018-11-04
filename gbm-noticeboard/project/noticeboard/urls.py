from django.conf.urls import url, include
from django.urls import path

from project.noticeboard import views

urlpatterns = [
    path('noticeboard/', views.NoticeboardView.as_view(), name='Noticeboard'),
]
