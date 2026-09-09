import os

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def feed(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        if image:
            extension = os.path.splitext(image.name)[1].lower()

            allowed_extensions = [".jpg", ".jpeg", ".png"]

            if extension not in allowed_extensions:
                error = "Only JPG, JPEG, and PNG files are allowed."

            else:
                Post.objects.create(
                    username=username, description=description, image=image
                )

                return redirect("feed")

    posts = Post.objects.all().order_by("-id")

    return render(request, "posts/feed.html", {"posts": posts, "error": error})


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    post.likes += 1
    post.save()

    return redirect("feed")
