# Django ORM CRUD Lab

## Overview

This lab demonstrates basic CRUD operations using Django ORM with a
`Product` model.

## Product Model

The `Product` model contains:

-   `name`
-   `price`
-   `stock`
-   `is_active`

## CRUD Operations

### 1. Create

Created three products with different prices and stock levels.

``` python
Product.objects.create(name="Keyboard", price=250, stock=10)
Product.objects.create(name="Mouse", price=100, stock=0)
Product.objects.create(name="Monitor", price=800, stock=5)
```

### 2. Read

Retrieved all products:

``` python
Product.objects.all()
```

Filtered active products with stock greater than zero:

``` python
Product.objects.filter(is_active=True, stock__gt=0)
```

Searched for products by name:

``` python
Product.objects.filter(name__icontains="key")
```

Retrieved one product using its primary key:

``` python
Product.objects.get(pk=1)
```

Handled a missing product:

``` python
try:
    product = Product.objects.get(pk=100)
    print(product)
except Product.DoesNotExist:
    print("Product not found")
```

### 3. Update

Updated a single product using `save()`:

``` python
product = Product.objects.get(pk=1)
product.price = 300
product.stock = 15
product.save(update_fields=["price", "stock"])
```

Updated matching products using `QuerySet.update()`:

``` python
Product.objects.filter(stock=0).update(is_active=False)
```

### 4. Delete

Deleted inactive products with zero stock:

``` python
Product.objects.filter(
    is_active=False,
    stock=0
).delete()
```

## Key Concepts

-   `create()` creates and saves a new object.
-   `all()` returns all objects.
-   `filter()` returns a QuerySet containing matching objects.
-   `get()` returns one object and raises `DoesNotExist` when no
    matching object exists.
-   `save()` saves changes made to a model instance.
-   `update()` updates matching records directly in the database.
-   `delete()` removes matching records from the database.
-   `__gt` means greater than.
-   `__icontains` performs a case-insensitive contains search.

## Important Note

Changing values on a model instance does not update the database until
`save()` is called.

``` python
product.price = 300
product.stock = 15
product.save()
```

## Final Result

After completing the CRUD operations, the remaining products were:

-   Keyboard
-   Monitor
