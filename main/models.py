from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from .managers import MyUserManager

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_shop_owner = models.BooleanField(default=False, verbose_name='Are you a shop Owner?', blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_shop_owner']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(blank=False)


class ShopOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.FloatField(blank=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_shop_owner:
            ShopOwner.objects.create(user=instance, credit = 0.0)
        else:
            Customer.objects.create(user=instance, balance=20.0)


class Order(models.Model):
    time = models.DateTimeField()
    isServed = models.BooleanField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bill = models.FloatField()


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
