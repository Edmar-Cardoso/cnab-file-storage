from django.db import models

class Store(models.Model):
    total = models.FloatField(default=0)
    cpf = models.CharField(max_length=11)
    owner = models.CharField(max_length=14)
    name = models.CharField(max_length=19)
