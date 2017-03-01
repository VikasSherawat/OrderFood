from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()


class Customer(User):
    balance = models.FloatField()


class Order(models.Model):
    time = models.DateTimeField()
    isServed = models.BooleanField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
