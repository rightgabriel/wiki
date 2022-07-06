from django import forms

# from https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349237-capture-user-input-with-django-forms


class ContactUsForm(forms.Form):
   title = forms.CharField(required=False)
   content = forms.CharField(max_length=1000)