from django.shortcuts import render
import markdown2
from django.shortcuts import redirect
from pages.models import Pages


def getPageDB (request, pagename):
    urlsplit = splitUrl(request)
    try:
        if "promos" in urlsplit[0]:
            page = Pages.objects.get(name="promos/" + pagename)
            url = "pages/page-promos.html"
        elif "faq" in urlsplit[0]:
            page = Pages.objects.get(name="faq/" + pagename)
            url = "pages/page.html"
        else:
            page = Pages.objects.get(name=pagename)
            url = "pages/page.html"
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
    return render(request, url, context)


def getPages(request):
    paths = splitUrl(request)[0]
    lenght = splitUrl(request)[1]
    page = paths[lenght - 1] if paths[lenght - 1] != '' else 'index'
    return render(request, "pages/{}.html".format(page))


def getContact(request):
    context = {}
    return render(request, "pages/contact.html", context)


def splitUrl (request):
    return [request.path.split("/"), len(request.path.split("/"))]
