from django.db import models

# Create your models here.

class Pages(models.Model):
    name = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    imgTop = models.CharField(max_length=200)
    imgRight = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    visibleImgLeft = models.BooleanField(default=True)

    def __str__(self):
        return self.name
