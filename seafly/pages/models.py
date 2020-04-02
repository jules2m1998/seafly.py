from django.db import models
from django import forms


# Create your models here.

class Pages(models.Model):
    name = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    title_en = models.CharField(max_length=200, default='')
    title_th = models.CharField(max_length=200, default='')
    imgTop = models.CharField(max_length=200)
    imgRight = models.CharField(max_length=200)
    content = models.CharField(max_length=3000, default='')
    content_en = models.CharField(max_length=3000, default='')
    content_th = models.CharField(max_length=3000, default='')
    visibleImgRight = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)


class Pages_Form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    content_en = forms.CharField(widget=forms.Textarea)
    content_th = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Pages
        fields = '__all__'