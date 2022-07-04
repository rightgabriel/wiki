import random
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
import markdown2
from markdown2 import Markdown
from os import listdir
from os.path import isfile, join
from random import randint



from . import util

files = [f for f in listdir("entries") if isfile(join("entries", f))]



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):

    cap = title.capitalize()

    try:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content":   markdown2.markdown(util.get_entry(title)),
            "cap": cap
        })
    except:
        return render(request, "encyclopedia/404.html", {
            "entries": util.list_entries(),
           
       })


def add(request):
    return render(request, "encyclopedia/new.html", {
        "entries": util.list_entries()
    })