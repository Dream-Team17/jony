from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.faculty}'



class Faculty(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_1 = models.ImageField(null=True, default='', blank=True)
    image_2 = models.ImageField(null=True, default='', blank=True)
    image_3 = models.ImageField(null=True, default='', blank=True)
    icon = models.ImageField(null=True, default='', blank=True)

    def __str__(self):
        return f'{self.author.username}_{self.title}'
