from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry" ),
    path("", views.search, name="search"),
    path("add/", views.add, name="create")
]
