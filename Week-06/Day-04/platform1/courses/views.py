from django.shortcuts import render


def course_list(request):
    return render(request, "courses/list.html")


def course_detail(request, course_id):
    return render(request, "courses/detail.html", {"course_id": course_id})


def category(request, category_name):
    return render(request, "courses/category.html", {"category_name": category_name})
