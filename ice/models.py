from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Moms(models.Model):
    name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)


class Dads(models.Model):
    name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)


class Children(models.Model):
    name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    mom = models.OneToOneField(Moms, on_delete=models.CASCADE)
    dad = models.OneToOneField(Dads, on_delete=models.CASCADE)


class IceCream(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.IntegerField(null=True)


class Kiosk(models.Model):
    seller = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE)
