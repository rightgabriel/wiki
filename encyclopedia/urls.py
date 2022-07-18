from django.urls import path
import markdown2

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="title"),
    path("<str:title>", views.entry, name="title"),
    path('new/', views.contact, name='contact'),
    path('edit/', views.edit2, name='edit2'),
    path("wiki/", views.q, name="q"),
    path("random/", views.random_page, name="random")
]
