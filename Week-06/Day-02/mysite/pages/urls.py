from django.contrib import admin
from django.urls import path
from pages.views import index, faq, team


urlpatterns = [
    path("index.html/", index, name="index"),
    path("faq.html/", faq, name="faq"),
    path("team.html/", team, name="team"),
]
