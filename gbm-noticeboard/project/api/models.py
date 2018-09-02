from django.db import models



# Create your models here.

class Missionary(models.Model):
    friendly_name = models.CharField(max_length=40)
    email = models.EmailField()
    class Meta:
            verbose_name_plural = "missionaries"
            
class Update(models.Model):
    missionary = models.ForeignKey(Missionary, on_delete=models.PROTECT)
    date_of_update = models.DateField()
    date_publish_start = models.DateField()
    date_publish_end = models.DateField()
    content = models.TextField()
