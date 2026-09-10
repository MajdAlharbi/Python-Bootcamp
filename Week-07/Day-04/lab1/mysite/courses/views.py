from django.shortcuts import render

courses = [
    {
        "id": 1,
        "name": "Python Basics",
        "category": "backend",
        "difficulty": "beginner",
    },
    {
        "id": 2,
        "name": "Django Basics",
        "category": "backend",
        "difficulty": "intermediate",
    },
    {
        "id": 3,
        "name": "HTML Basics",
        "category": "frontend",
        "difficulty": "beginner",
    },
]


def course_list(request):
    category = request.GET.get("category", "")
    difficulty = request.GET.get("difficulty", "")
    page = int(request.GET.get("page", "1"))

    filtered_courses = courses

    if category:
        filtered_courses = [
            course for course in filtered_courses if course["category"] == category
        ]

    if difficulty:
        filtered_courses = [
            course for course in filtered_courses if course["difficulty"] == difficulty
        ]

    per_page = 2

    start = (page - 1) * per_page
    end = start + per_page

    paginated_courses = filtered_courses[start:end]

    return render(
        request,
        "courses/courses.html",
        {
            "courses": paginated_courses,
            "page": page,
        },
    )


def course_detail(request, id):
    selected_course = None

    for item in courses:
        if item["id"] == id:
            selected_course = item
            break

    tab = request.GET.get("tab", "overview")

    return render(
        request,
        "courses/courses.html",
        {
            "courses": courses,
            "course": selected_course,
            "tab": tab,
        },
    )
