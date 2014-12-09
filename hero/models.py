from django.db import models

# Create your models here.
class Hero (models.Model):
    title = models.CharField (max_length=70)
    vocation = models.CharField (max_length=70)
    description = models.CharField(max_length=200)
    eptitude = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
