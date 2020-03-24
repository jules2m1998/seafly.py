from django.shortcuts import render
import markdown2
from django.shortcuts import redirect
from pages.models import Pages


def index(request):
    return render(request, "pages/index.html")


def getPage(request, pagename):
    try:
        page = Pages.objects.get(name=pagename)
    except:
        return redirect("/")

    page.content = markdown2.markdown(page.content)
    context = {
        'page': page
    }
    return render(request, "pages/page.html", context)


def getPromos(request):
    return render(request, "pages/promos.html")


def getFaq (request):
    return render(request, "pages/faq.html")