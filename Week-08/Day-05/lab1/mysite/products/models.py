from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveBigIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    available_from = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    prodect_image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name
