from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('blogs/', views.blogs, name="blogs"),
    path('blog/<int:Id>/', views.blog, name="blog")
]