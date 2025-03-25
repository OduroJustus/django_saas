from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

import pathlib

# Create your views here.
this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    qs = PageVisit.objects.all() # All page visits
    page_visit_qs = PageVisit.objects.filter(path=request.path) # Current page
    my_title = "Home Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": qs.count(),
        "total_visit_count": qs.count(),
        "percent_of_total": (page_visit_qs.count() / qs.count()) * 100,
    }
    html_template = "home.html"
    # PageVisit.objects.create(path=request.path, user=request.user)
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()  # All page visits
    page_visit_qs = PageVisit.objects.filter(path=request.path)  # Current page
    try:
       percent = (page_visit_qs.count() / qs.count()) * 100
    except:
        percent = 0
    my_title = "About Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": qs.count(),
        "total_visit_count": qs.count(),
        "percent_of_total": percent,
    }
    html_template = "about.html"
    # PageVisit.objects.create(path=request.path, user=request.user)
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)