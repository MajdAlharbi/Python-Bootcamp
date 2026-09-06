from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request, "accounts/register.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        request.session["registered_username"] = username
        request.session["registered_password"] = password

        return redirect("profile")


class ProfileView(View):
    def get(self, request):
        username = request.session.get("username")

        if not username:
            return redirect("login")

        context = {"username": username}

        return render(request, "accounts/profile.html", context)


class LoginView(View):
    def get(self, request):
        return render(request, "accounts/login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        saved_username = request.session.get("registered_username")
        saved_password = request.session.get("registered_password")

        if username == saved_username and password == saved_password:
            request.session["username"] = username
            return redirect("profile")

        context = {"error": "Invalid username or password"}

        return render(request, "accounts/login.html", context)


def status(request):
    return JsonResponse({"status": "ok"})
