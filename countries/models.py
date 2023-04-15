from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()

    def __str__(self):
        return f'{self.author.username}_{self.title}'
