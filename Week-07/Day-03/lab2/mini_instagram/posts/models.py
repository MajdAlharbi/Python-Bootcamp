from django.db import models
from django.core.validators import FileExtensionValidator


class Post(models.Model):
    username = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to="posts/",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])],
    )
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.username
