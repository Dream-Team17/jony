from django.db import models

class MainImage_2(models.Model):
    image = models.ImageField(null=True, default='', blank=True)
