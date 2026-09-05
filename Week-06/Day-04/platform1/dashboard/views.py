from django.shortcuts import render
from django.views import View


def home(request):
    return render(request, "dashboard/home.html")


class ReportsView(View):
    def get(self, request):
        return render(request, "dashboard/reports.html")
