from django.db import models


class Dish(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    preparation_time = models.DurationField()
    date_added = models.DateField('date added', auto_now_add=True)
    date_modified = models.DateField('date modified', auto_now=True)
    is_vegan = models.BooleanField()
    
    class Meta:
            verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField()
    date_added = models.DateField('date added', auto_now_add=True)
    date_modified = models.DateField('date modified', auto_now=True)
    dishes = models.ManyToManyField(Dish, blank=True)

    class Meta:
            verbose_name_plural = "Menus"

    def __str__(self):
        return self.name
