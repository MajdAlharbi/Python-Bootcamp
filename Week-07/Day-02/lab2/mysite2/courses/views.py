from django.shortcuts import render


courses = [
    {
        "id": 1,
        "name": "python ",
        "level": "beginner",
        "student_count": 25,
        "description": "Learn Python programming from the beginning.",
        "image": "images/python.png",
    },
    {
        "id": 2,
        "name": "html",
        "level": "intermediate",
        "student_count": 0,
        "description": "Learn how to build web pages.",
        "image": "images/HTML.png",
    },
    {
        "id": 3,
        "name": "css",
        "level": "beginner",
        "student_count": 18,
        "description": "Learn how to build styled web pages.",
        "image": "images/CSS.png",
    },
]


def home(request):
    context = {
        "username": "Majd",
    }

    return render(request, "courses/home.html", context)


def courses_list(request):
    context = {
        "username": "Majd",
        "courses": courses,
    }

    return render(request, "courses/courses.html", context)


def course_detail(request, course_id):
    selected_course = None

    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    context = {
        "course": selected_course,
    }

    return render(request, "courses/course_detail.html", context)
