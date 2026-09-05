from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("list/", views.course_list, name="list_courses"),
    path("detail/<int:course_id>/", views.course_detail, name="course_detail"),
    path("category/<str:category_name>/", views.category, name="course_category"),
]
