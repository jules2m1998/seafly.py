from django.shortcuts import render
import markdown2
from django.shortcuts import redirect
from pages.models import Pages


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


def getPages(request):
    paths = request.path.split("/")
    lenght = len(request.path.split("/"))
    page = paths[lenght - 1] if paths[lenght - 1] != '' else 'index'
    return render(request, "pages/{}.html".format(page))
