from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path("index", views.index, name="index"),
]
