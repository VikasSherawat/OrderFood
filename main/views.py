from django.shortcuts import render
from .Customer.views import *
from .ShopOwner.views import *
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index page.")