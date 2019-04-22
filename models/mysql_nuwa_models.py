from django.db import models

class Person(models.Model):
    id = models.ImageField()
    name = models.CharField(max_length=64)
    purview = models.ImageField()
    modify_time = models.DateTimeField(auto_now_add=False, auto_now=True)