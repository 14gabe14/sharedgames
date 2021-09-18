from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This should be the shared games index.")

def detail(request, group_id):
    return HttpResponse("The code is %s." % group_id)

def example(request):
    return HttpResponse("This is an example")