from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    groups = models.ForeignKey('Group', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.groups}'


class Group(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.author.username}_{self.title}'

