from django.urls import path
from . import views
from .views import home
from .views import index

urlpatterns = [
    path('', home, name='home'),
    path('grades/', views.index, name='index'),
    
]