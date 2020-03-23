from django.contrib import admin
from .models import Pages

# Register your models here.
admin.site.site_header = 'Page d\'administration'
admin.site.register(Pages)
