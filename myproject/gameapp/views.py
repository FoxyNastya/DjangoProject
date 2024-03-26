from random import choice, random, randint

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello world!!!')


def orel_reshka(request):
    return HttpResponse(choice(['Орел', 'Решка']))


def kub(request):
    return HttpResponse(str(randint(1, 7)))


def numbers(request):
    return HttpResponse(str(randint(0, 1000)))

