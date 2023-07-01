from django.db import models

# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    habitat = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.name