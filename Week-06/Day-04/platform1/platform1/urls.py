from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("courses/", include("courses.urls")),
    path("", include("dashboard.urls")),
    path("payments/", include("payments.urls")),
    path("users/", include("users.urls")),
]
