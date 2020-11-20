from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render


posts = [
    {
        'Name' : 'Aaron Coccagna',
        'grade' : 'A+',
        'date_posted' : 'November 20th 2020'
    },

    {
        'Name' : 'John Smith',
        'grade' : 'B+',
        'date_posted' : 'November 20th 2020'
    }


]

def index(request):
    context = {
        'posts' : posts
    }
    return render(request, "grades/grades.html", context)

def home(request):
    return render(request, "grades/home.html")