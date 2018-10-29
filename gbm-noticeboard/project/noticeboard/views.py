from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView

# Create your views here.

from django.contrib.auth.models import User
from .models import Missionary, Update

import datetime

class NoticeboardView(TemplateView):
    template_name = 'noticeboard/noticeboard.html'

    def get_context_data(self, **kwargs):
         context = super(NoticeboardView, self).get_context_data(**kwargs)
         context['updates'] = Update.objects.all()[:2]

         date = datetime.date.today()
         start_week = date - datetime.timedelta(date.weekday())
         end_week = start_week + datetime.timedelta(6)
         context['updates_this_week'] = Update.objects.filter(date_publish__range=[start_week, end_week]).exclude(hidden=True)
         context['missionaries'] = Missionary.objects.all()[:4]
         return context
