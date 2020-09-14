from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="", blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="", blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    pub_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(default="")

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name



