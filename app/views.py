from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request, "aboutus.html")

def blogs(request):
    blogs_list = Blog.objects.all()
    return render(request, "blogs.html", {
        "blogs": blogs_list,
    })

def blog(request, Id):
    return render(request, "blog.html")