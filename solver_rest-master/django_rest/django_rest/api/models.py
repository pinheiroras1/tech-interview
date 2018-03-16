from django.db import models


class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name


class Carts(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.IntegerField(max)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()    
    cart_id = models.ForeignKey(Carts, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Articles, on_delete=models.CASCADE)

