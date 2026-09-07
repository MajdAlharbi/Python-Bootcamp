from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("courses/", views.courses_list, name="courses"),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
]
