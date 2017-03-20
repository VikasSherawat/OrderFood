from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()


class Customer(User):
    balance = models.FloatField()


class Order(models.Model):
    order_date = models.DateTimeField()
    isServed = models.BooleanField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bill = models.FloatField()


class ShopOwner(User):
    balance = models.FloatField()


class SubscriptionType(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    duration = models.IntegerField()


class Subscription(models.Model):
    starting_date = models.DateTimeField()
    end_date = models.DateTimeField()
    subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)


class Location(models.Model):
    area = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Shop(models.Model):
    name = models.CharField(max_length=20)
    shop_owner = models.ForeignKey(ShopOwner, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Category(models.Model):
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    shops = models.ManyToManyField(Shop)


class FoodItem(models.Model):
    price = models.FloatField()
    orders = models.ManyToManyField(Order)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    grade = models.FloatField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writer')
    user_commented = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_commented')


class ManualTransaction(models.Model):
    amount_money = models.FloatField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
