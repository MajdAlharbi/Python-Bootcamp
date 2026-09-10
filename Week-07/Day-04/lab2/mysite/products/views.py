from django.http import Http404
from django.shortcuts import render

products = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "electronics",
        "price": 3500,
        "rating": 4.8,
        "description": "A powerful laptop for work and study.",
    },
    {
        "id": 2,
        "name": "Headphones",
        "category": "electronics",
        "price": 300,
        "rating": 4.5,
        "description": "Wireless headphones with clear sound.",
    },
    {
        "id": 3,
        "name": "Python Book",
        "category": "books",
        "price": 120,
        "rating": 4.7,
        "description": "A beginner-friendly Python programming book.",
    },
    {
        "id": 4,
        "name": "Backpack",
        "category": "accessories",
        "price": 180,
        "rating": 4.2,
        "description": "A practical backpack for everyday use.",
    },
]


def product_list(request):
    category = request.GET.get("category", "")
    min_price = request.GET.get("min_price", "")
    q = request.GET.get("q", "")
    sort = request.GET.get("sort", "name")
    page = request.GET.get("page", "1")

    filtered_products = products

    if category:
        filtered_products = [
            product for product in filtered_products if product["category"] == category
        ]

    if min_price:
        try:
            min_price = float(min_price)

            filtered_products = [
                product
                for product in filtered_products
                if product["price"] >= min_price
            ]
        except ValueError:
            pass

    if q:
        filtered_products = [
            product
            for product in filtered_products
            if q.lower() in product["name"].lower()
        ]

    allowed_sort = ["price", "rating", "name"]

    if sort not in allowed_sort:
        sort = "name"

    filtered_products = sorted(filtered_products, key=lambda product: product[sort])

    try:
        page = int(page)
    except ValueError:
        page = 1

    per_page = 2

    start = (page - 1) * per_page
    end = start + per_page

    paginated_products = filtered_products[start:end]

    return render(
        request,
        "products/prodects.html",
        {
            "products": paginated_products,
            "page": page,
            "category": category,
            "min_price": min_price,
            "q": q,
            "sort": sort,
        },
    )


def product_detail(request, id):
    selected_product = None

    for product in products:
        if product["id"] == id:
            selected_product = product
            break

    if selected_product is None:
        raise Http404("Product not found")

    tab = request.GET.get("tab", "description")

    return render(
        request,
        "products/prodects.html",
        {
            "products": products,
            "product": selected_product,
            "tab": tab,
        },
    )
