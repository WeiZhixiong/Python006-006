from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index),
    path("movie/", include("movie.urls")),
]