from django.shortcuts import render
from django.conf import settings
import os


def upload(request):
    image_url = None

    if request.method == "POST":
        uploaded_image = request.FILES.get("image")

        if uploaded_image:
            upload_path = os.path.join(
                settings.MEDIA_ROOT,
                uploaded_image.name
            )

            with open(upload_path, "wb+") as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)

            image_url = settings.MEDIA_URL + uploaded_image.name

    return render(request, "upload.html", {
        "image_url": image_url
    })