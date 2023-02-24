from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)

class Admin(models.Model):
    first_admin_name = models.CharField(max_length=15)
    last_admin_name = models.CharField(max_length=20)

class Orders(models.Model):
    Product_name = models.CharField(max_length=50)
    Product_price = models.IntegerField()
    location = models.TextField()



