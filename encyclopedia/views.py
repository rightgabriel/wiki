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
from django import forms
from encyclopedia.forms import ContactUsForm
from django.core.mail import send_mail
import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import redirect

from . import util

files = [f for f in listdir("entries") if isfile(join("entries", f))]



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "url": "entries"
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

# partially from https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349237-capture-user-input-with-django-forms

def contact(request):
  
    if request.method == 'POST':
      # create an instance of our form, and fill it with the POST data
        form = ContactUsForm(request.POST)
       
        if form.is_valid():

            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            filename = f"entries/{title}.md"

            if default_storage.exists(filename):
               

                return render(request,
                    'encyclopedia/404.html',)        
            else:
           
                util.save_entry(title, content)
                return (entry(request,title)) # add this return statement
            
    else:
  # this must be a GET request, so create an empty form
        form = ContactUsForm() # instantiate a new form here
    return render(request,
          'encyclopedia/new.html',
          {'form': form}) # pass that form to the template


def edit(request, *args, **kwargs):
    if request.method == 'POST':
      # create an instance of our form, and fill it with the POST data
        form = ContactUsForm(request.POST)
       
        if form.is_valid():

            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            filename = f"entries/{title}.md"

            if default_storage.exists(filename):
                         
                util.save_entry(title, content)
                return (entry(request,title)) # add this return statement
            
    else:
  # this must be a GET request, so create an empty form
        form = ContactUsForm() # instantiate a new form here
    return render(request,
          'encyclopedia/edit.html',
          {'form': form}) # pass that form to the template
                
def edit2(request):
    if request.method == 'POST':
      # create an instance of our form, and fill it with the POST data
        form = ContactUsForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            filename = f"entries/{title}.md"
            return render(request, "encyclopedia/edit.html", {
                "title": title,
                "content":   markdown2.markdown(util.get_entry(title)),
           
             })

def list_q(q1):
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if q1 in filename))

def q(request):
    
 
    if request.method == 'POST':
        q1 = request.POST['q']
        cap = q1.capitalize()
        entries = util.list_entries(),

        try:
            return render(request, "encyclopedia/entry.html", {
                "q1": q1,
                "cap": cap,
                "content":   markdown2.markdown(util.get_entry(q1)),
                "has": all([char in entries for char in q1]),
                })
        except:
            return render(request, "encyclopedia/search.html", {
                "q1": q1,
                "cap": cap,
                "entries": util.list_entries(),
                "query": list_q(q1)
                })




def random_page(request):
    entries = util.list_entries() # list of wikis
    selected_page = random.choice(entries)
    return redirect("title", title=selected_page)