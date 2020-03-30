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

    switcher = {
        'fr': [page.title, page.content],
        'en': [page.title_en, page.content_en],
        'th': [page.title_th, page.content_th],
    }
    page.title = switcher.get(request.LANGUAGE_CODE, '')[0]
    page.content = switcher.get(request.LANGUAGE_CODE, '')[1]
    page.content = markdown2.markdown(page.content)
    context = {
        'page': page
    }
    return render(request, "pages/page.html", context)


def getPromos(request):
    return render(request, "pages/promos.html")


def getFaq(request):
    return render(request, "pages/faq.html")


def getContact(request):
    return render(request, "pages/contact.html")


def getConvert(request):
    return render(request, "pages/conversion.html")


def getDevis(request):
    return render(request, "pages/devis.html")


def getPromotions(request, pagename):
    try:
        page = Pages.objects.get(name="promos/" + pagename)
    except:
        return redirect("/")

    page.content = markdown2.markdown(page.content)
    context = {
        'page': page
    }
    return render(request, "pages/page-promos.html", context)
