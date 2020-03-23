from django.db import models
from django import forms


# Create your models here.

class Pages(models.Model):
    name = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    imgTop = models.CharField(max_length=200)
    imgRight = models.CharField(max_length=200)
    content = models.CharField(max_length=3000, default=' ')
    visibleImgRight = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Pages_Form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Pages
        fields = '__all__'