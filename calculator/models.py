from django.db import models

# Create your models here.
class Operation(models.Model):
    x = models.FloatField(default=0)
    y = models.FloatField(default=0)
    op = models.CharField(max_length=30)