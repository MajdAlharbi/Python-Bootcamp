from django.contrib import admin
from django.urls import path
from libary import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("<int:id>/", views.book_detail, name="book_detail"),
]
