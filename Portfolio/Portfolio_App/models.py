from django.db import models

# Create your models here.
class Response_m(models.Model):
    name = models.CharField(max_length = 100 )
    email = models.EmailField()
    comment =models.CharField(max_length = 1000)
