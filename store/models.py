from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_cat")
    cat_name = models.CharField(max_length=255, verbose_name="Category Name")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="prod_user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="prod_cat")
    prod_name = models.CharField(max_length=255, verbose_name="Product Name")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prod_name
