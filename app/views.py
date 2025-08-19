from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    projects = Project.objects.all()
    future_projects = Future_projects.objects.all()
    return render(request, "index.html", {
        "projects": projects,
        "future_projects": future_projects,
    })

def aboutus(request):
    return render(request, "aboutus.html")

def blogs(request):
    blogs_list = Blog.objects.all()
    return render(request, "blogs.html", {
        "blogs": blogs_list,
    })

def blog(request, Id):
    return render(request, "blog.html")

def contact(request):
    return render(request, "contact.html")

def projectinfo(request, Id):
    return render(request, "projectinfo.html")

def projects(request):
    return render(request, "projects.html")

def donation(request):
    return render(request, "donation.html")