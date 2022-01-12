from django.db import models

class Tick(models.Model):

    class Meta:
        db_table = 'tick'

    epoch_timestamp = models.BigIntegerField()
    symbol = models.CharField(max_length=50)
    value = models.BigIntegerField()

    def __str__(self):
        return f"{self.epoch_timestamp} - {self.symbol} - {self.value}" 