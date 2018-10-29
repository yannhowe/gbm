from django.db import models
from datetime import datetime
# Create your models here.

class Missionary(models.Model):
    friendly_name = models.CharField(max_length=40)
    email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    profile = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(blank=True)
    upcoming = models.TextField(null=True, blank=True)
    prayer = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "missionaries"

    def __str__(self):
        return '%s - %s' % (self.friendly_name, self.country)

class Update(models.Model):
    missionary = models.ForeignKey(Missionary, on_delete=models.PROTECT)
    date_of_update = models.DateField(default=datetime.now)
    date_publish = models.DateField(default=datetime.now)
    content = models.TextField(null=True, blank=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return '%s | letter date: %s | publish week of: %s' % (self.missionary, self.date_of_update, self.date_publish)
