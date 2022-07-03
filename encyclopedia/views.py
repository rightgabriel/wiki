from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
import markdown2
from markdown2 import Markdown


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):

    cap = title.capitalize()

    
   
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content":   markdown2.markdown(util.get_entry(title)),
        "cap": cap

    })
  


   