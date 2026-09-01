from django.shortcuts import render

books = [
    {"id": 1, "title": "Python", "author": "Majd"},
    {"id": 2, "title": "Django", "author": "Sara"},
]


def book_list(request):
    context = {"books": books}
    return render(request, "libary/book_list.html", context)


def book_detail(request, id):
    book = None
    for b in books:
        if b["id"] == id:
            book = b
            break
    return render(request, "libary/book_detail.html", {"book": book})
