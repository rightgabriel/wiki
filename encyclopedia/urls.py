from django.urls import path
import markdown2

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.entry, name="entry")
]
