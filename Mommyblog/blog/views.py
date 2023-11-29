from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """ home page """
    return HttpResponse("<h1> hello jailan </h1>")

def about(request):
    """about page for blog"""
    return HttpResponse("<h2> about page </h2>")
