from django.db import models


class File(models.Model):
    transaction_type = models.IntegerField()
    transaction_at = models.DateField()
    value = models.FloatField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    transaction_hour = models.CharField(max_length=6)
    owner = models.CharField(max_length=14)
    name = models.CharField(max_length=19)
    file = models.CharField(max_length=8100)
