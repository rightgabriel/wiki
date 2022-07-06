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

"""
def add(request):
   #  task = util.save_entry("title", "f")

   
      
    if request.method == "POST":
        return render(request, "encyclopedia/new.html", {
            "task": util.save_entry("one", "two")
    })
    
       
            # If the form is invalid, re-render the page with existing information.
    else: 

        return render(request, "encyclopedia/new.html", {
            
    })

"""



