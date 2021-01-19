from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Support(models.Model):
    ticker = models.CharField(max_length=100)
    market = models.CharField(max_length=100)
    current_price = models.IntegerField()
    current_date = models.CharField(max_length=100)
    s1_date = models.CharField(max_length=100)
    s1_price = models.IntegerField()
    s1_diff = models.IntegerField()
    s2_date = models.CharField(max_length=100)
    s2_price = models.IntegerField()
    s2_diff = models.IntegerField()
