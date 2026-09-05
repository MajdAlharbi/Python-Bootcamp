from django.urls import path
from . import views

app_name = "blog"


urlpatterns = [
    path("", views.list, name="list"),
    path("detail/<int:id>/", views.detail, name="detail"),
    path("category_routes/<slug:slug>/", views.category_routes, name="category_routes"),
]
