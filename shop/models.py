from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()  # Цена в центах

    def __str__(self):
        return str(self.price)

    def human_price(self):
        return self.price / 100


class Order(models.Model):
    pk_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.pk_item)

    def get_absolute_url(self):
        return reverse('order', kwargs={'order': self.pk})

