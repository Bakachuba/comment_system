from PIL import Image as PILImage

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='post_picture')
    caption = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username}\'s Post - {self.caption}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = PILImage.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.caption}'
