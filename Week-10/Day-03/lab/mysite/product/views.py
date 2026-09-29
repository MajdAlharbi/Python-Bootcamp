from django.http import HttpResponse


def index(request):
    return HttpResponse("product is wired up.")
