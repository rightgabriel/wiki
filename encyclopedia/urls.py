from django.urls import path
import markdown2

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="title"),
    path('new/', views.contact, name='contact'),
    path('edit/', views.edit, name='edit'),
    path("search/", views.q, name="q")
]
