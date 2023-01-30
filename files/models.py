from django.db import models


class File(models.Model):
    transaction_type = models.CharField(max_length=30)
    transaction_at = models.DateField()
    value = models.FloatField()
    card = models.CharField(max_length=12)
    transaction_hour = models.CharField(max_length=6)
    file = models.CharField(max_length=8100)

    store = models.ForeignKey(
        "stores.Store", on_delete=models.CASCADE, related_name="files"
    )
