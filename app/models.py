from django.db import models

# Create your models here.

class Car(models.Model):
    model = models.TextField()
    year = models.IntegerField()
    mileage = models.IntegerField()


    def __str__(self):
        return f'{self.model} ({self.year})'
