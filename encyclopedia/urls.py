from django.urls import path
import markdown2

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="title"),
    path("new/", views.add, name="add"),


]
