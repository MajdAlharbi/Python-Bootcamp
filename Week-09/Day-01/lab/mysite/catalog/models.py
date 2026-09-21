from django.db import models
from typing import ClassVar


class Product(models.Model):
    class Category(models.TextChoices):
        ELECTRONICS = "electronics", "Electronics"
        FOOD = "food", "Food"
        ACCESSORY = "accessory", "Accessory"

    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=30, unique=True)

    category = models.CharField(
        max_length=20, choices=Category.choices, default=Category.ACCESSORY
    )

    description = models.TextField(blank=True)

    stock = models.PositiveIntegerField(default=0)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def is_available(self):
        return self.is_active and self.stock > 0

    def inventory_value(self):
        return self.price * self.stock

    def __str__(self):
        return f"{self.name} ({self.sku})"

    class Meta:
        ordering = ["category", "name"]

    verbose_name = "Product"
    verbose_name_plural = "Products"

    indexes = [
        models.Index(fields=["category", "is_active"]),
    ]

    constraints: ClassVar[list[models.BaseConstraint]] = [
        models.CheckConstraint(
            condition=models.Q(price__gte=0),
            name="product_price_non_negative",
        ),
        models.CheckConstraint(
            condition=models.Q(stock__gte=0),
            name="product_stock_non_negative",
        ),
    ]
