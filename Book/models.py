from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    author = models.CharField(max_length=40, null=True)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @property
    def short_description(self):
        return f'{self.description[:40]}...'
