from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This Is the Home Page")
def muhib(request):
    return HttpResponse("<h1 style='color: green;'>This Is a Url Page </h1>")
def auth(request):
    return HttpResponse("Creacted By MUHIB-143")
