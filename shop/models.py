from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()  # Цена в центах

    def __str__(self):
        return str(self.price)

    def human_price(self):
        return self.price / 100