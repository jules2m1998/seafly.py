from django.http import HttpResponse
from django.shortcuts import render
from pages.models import Pages
from django.template import loader


def index(request):
    return render(request, "pages/index.html")


def getPage(request, pagename):
    page = Pages.objects.get(name=pagename)
    context = {
        'page': page
    }
    return render(request, "pages/page.html", context)
