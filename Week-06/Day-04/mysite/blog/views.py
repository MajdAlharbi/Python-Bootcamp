from django.shortcuts import render


def list(request):
    return render(request, "blog/list.html")


def detail(request, id):
    return render(request, "blog/detail.html", {"id": id})


def category_routes(request, slug):
    return render(request, "blog/category_routes.html", {"slug": slug})
