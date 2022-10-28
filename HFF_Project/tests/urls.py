from django.urls import path
from . import views

app_name = "tests"

urlpatterns = [
    path("test1/<str:dnleh>/<str:rudeh>/", views.test1, name="test1"),
    path("test2/", views.test2, name="test2"),
]
