from django.shortcuts import render

# Create your views here.


def test1(request):
    return render(request, "tests/test1.html")


def test2(request):
    return render(request, "tests/test2.html")
