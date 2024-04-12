from django.db import models

# Create your models here.

class FlashInfo(models.Model):
    soft_ver = models.CharField(max_length=100)
    hil_id = models.CharField(max_length=100)
