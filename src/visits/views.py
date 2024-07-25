
from django.shortcuts import render
from .models import *


def home(request, *args, **kwargs):
    title = "Fuck you"
    queryset = PageVisits.objects.all()
    context = {
      'title': title,
      'count': queryset.count()
    }
    template = 'home.html'
    PageVisits.objects.create()
    return render(request, template, context)
