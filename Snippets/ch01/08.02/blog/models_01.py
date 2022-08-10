from django.db import models
from django.utils import timezone                                              # new


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)                       # new
    created = models.DateTimeField(auto_now_add=True)                          # new
    updated = models.DateTimeField(auto_now=True)                              # new

    def __str__(self):
        return self.title
