from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    from django.http import HttpResponse
    return HttpResponse('Hello world!!!')

