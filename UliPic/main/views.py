from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Picture, Material
from django.views.generic import DetailView

# Create your views here.
def index(response, id):
    pic = Picture.objects.get(id=id)
    return render(response, "main/base.html", {"pic":pic})

def PictureDetailView(response, pk):
    pic = Picture.objects.filter(id=pk)
    context = {"pic":pic}
    return render(response, "main/details_view.html", {"pic":pic})

def home(response):
    pic = Picture.objects.all()
    return render(response, "main/home.html", {"pic":pic})

def works(response):
    pic = Picture.objects.all()
    return render(response, "main/works.html", {"pic":pic})