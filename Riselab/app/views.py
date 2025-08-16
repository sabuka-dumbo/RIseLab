from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request, "aboutus.html")

def blogs(request):
    return render(request, "blogs.html")