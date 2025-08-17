from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('blogs/', views.blogs, name="blogs"),
    path('blog/<int:Id>/', views.blog, name="blog"),
    path('projectinfo/<int:Id>/', views.projectinfo, name="projectinfo"),
    path('projects/', views.projects, name="projects"),
    path('contact/', views.contact, name="contact"),
    path('donation/', views.donation, name="donation")
]