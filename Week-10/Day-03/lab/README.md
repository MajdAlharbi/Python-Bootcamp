# Day 03 -- Product Search QuerySet Lab

## Lab Objective

Build one reusable **Product Search QuerySet**, then refine it step by
step using Django ORM.

------------------------------------------------------------------------

## Requirements

Complete the following 8 steps:

1.  Start with active `Product` records.
2.  Keep products whose stock is above zero.
3.  Search `name` **OR** `SKU` using a `Q` object.
4.  Apply optional minimum and maximum prices.
5.  Filter by category name across the relationship.
6.  Order by `price`, then `name`, then `pk`.
7.  Return the first 10 results.
8.  Produce a `values()` result containing:
    -   `name`
    -   `sku`
    -   `price`

------------------------------------------------------------------------

## My Solution

### Setup Test Data

``` python
from product.models import Product, Category

electronics = Category.objects.create(name="Electronics")

Product.objects.create(
    name="Keyboard",
    sku="KB001",
    price=150,
    stock=10,
    is_active=True,
    category=electronics
)

Product.objects.create(
    name="Mouse",
    sku="MS001",
    price=80,
    stock=5,
    is_active=True,
    category=electronics
)

Product.objects.create(
    name="Monitor",
    sku="MN001",
    price=700,
    stock=0,
    is_active=True,
    category=electronics
)
```

### Product Search QuerySet

``` python
from django.db.models import Q

term = "Keyboard"
min_price = 50
max_price = 500
category = "Electronics"

# 1. Active products
products = Product.objects.filter(is_active=True)

# 2. Stock above zero
products = products.filter(stock__gt=0)

# 3. Search name OR SKU
products = products.filter(
    Q(name__icontains=term) |
    Q(sku__icontains=term)
)

# 4. Optional minimum and maximum prices
if min_price is not None:
    products = products.filter(price__gte=min_price)

if max_price is not None:
    products = products.filter(price__lte=max_price)

# 5. Filter by category name
if category:
    products = products.filter(category__name=category)

# 6. Order by price, name, then pk
products = products.order_by("price", "name", "pk")

# 7 & 8. Select fields and return first 10 results
results = products.values(
    "name",
    "sku",
    "price"
)[:10]

list(results)
```

------------------------------------------------------------------------

## Result

``` text
[{'name': 'Keyboard', 'sku': 'KB001', 'price': Decimal('150.00')}]
```

------------------------------------------------------------------------

## Notes

-   `filter()` refines a QuerySet.
-   `Q` allows complex conditions such as `OR`.
-   `__` is used for field lookups and relationships.
-   `order_by()` controls result ordering.
-   `[:10]` limits the result to the first 10 records.
-   `values()` returns selected fields as dictionaries.
-   `list(results)` evaluates the QuerySet.
