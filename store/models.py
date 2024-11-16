from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_cat")
    cat_name = models.CharField(max_length=255, verbose_name="Category Name")

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="prod_user")
    prod_name = models.CharField(max_length=255, verbose_name="Product Name")

    def __str__(self):
        return self.prod_name
