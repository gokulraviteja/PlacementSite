from django.db import models

# Create your models here.
class Object(models.Model):
    category=models.CharField(max_length=2000)
    branch=models.CharField(max_length=2000)
    comcount=models.IntegerField(default=0)

class Url(models.Model):
    recent=models.CharField(max_length=2000)

class Mate(models.Model):
    name=models.CharField(max_length=2000)
    category=models.CharField(max_length=2000)
    branch=models.CharField(max_length=2000)
    mobno=models.CharField(max_length=10)
