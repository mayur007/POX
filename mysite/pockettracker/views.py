#-*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render, get_object_or_404
from pockettracker.models import pocketdata

def index(request):
    # get the blog posts that are published
    pocketitems = pocketdata.objects.all()
    # now return the rendered template
    return render(request, 'pockettracker/index.html', {'pocketitems': pocketitems})

def pocketdatas(request, category):
    # get the Post object
    pocketcat = get_object_or_404(pocketdata, category = category)
    # now return the rendered template
    return render(request, 'pockettracker/pocket.html', {'pocketcat': pocketcat})
