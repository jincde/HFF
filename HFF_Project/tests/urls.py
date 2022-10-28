from django.urls import path
from . import views

app_name = "tests"

urlpatterns = [
    path("test1/", views.test1, name="test1"),
    path("test2/", views.test2, name="test2"),
]
