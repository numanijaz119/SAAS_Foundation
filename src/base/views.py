from django.shortcuts import render
from .models import PageVisit


def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)


def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0
    html_template = "base/home.html"
    my_context = {
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count(),
    }
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)
