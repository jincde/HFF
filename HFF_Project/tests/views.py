from django.shortcuts import render

# Create your views here.


def test1(request, dnleh, rudeh):
    context = {
        "endx": dnleh,
        "endy": rudeh,
    }
    return render(request, "tests/test1.html", context)


def test2(request):
    return render(request, "tests/test2.html")
