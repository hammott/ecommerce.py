from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,"homepage.html", {})
def aboutpage(request):
    return render(request,"aboutpage.html", {})
def contactpage(request):
    if request.method   ==  "POST":
        print(request.POST)
    return render(request,"contactpage.html", {})
