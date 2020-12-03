from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from .models import Post




def index(request):
    
    
    
    
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, "grades/grades.html", context)

def home(request):
    return render(request, "grades/home.html")