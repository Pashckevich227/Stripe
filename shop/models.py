from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.price)
