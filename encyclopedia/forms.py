from django import forms
from django.db import models
from django.forms import Textarea
from django.forms.widgets import Textarea

# from https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349237-capture-user-input-with-django-forms
# from https://docs.djangoproject.com/en/4.0/topics/forms/

class ContactUsForm(forms.Form):
    title = forms.CharField(required=False)

    content = forms.CharField(widget=forms.Textarea)
    

class eform(forms.Form):
    title = forms.CharField(required=False)

    content = forms.CharField(widget=forms.Textarea(attrs={"name": 'fe'}))
    