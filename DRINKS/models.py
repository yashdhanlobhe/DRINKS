from django.db import models
from matplotlib.pyplot import cla

class Drink(models.Model):
    name = models.CharField(max_length = 100)
    des = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


