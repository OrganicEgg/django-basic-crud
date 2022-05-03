from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("edit/<int:pk_id>", views.edit, name="edit"),
    path("delete/<int:pk_id>", views.delete, name="delete"),
]
