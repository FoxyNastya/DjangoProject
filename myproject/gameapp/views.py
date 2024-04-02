from random import choice, random, randint
from .models import Coin


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


#def index(request):
 #   return HttpResponse('Hello world!!!')


def coin(request):
    side = choice(['Орел', 'Решка'])
    arg = Coin(side=side)
    arg.save()
    return HttpResponse(str(side))


def kub(request):
    return HttpResponse(str(randint(1, 7)))


def numbers(request):
    return HttpResponse(str(randint(0, 1000)))


# def coin_values(request):
#     value = Coin.values()
#     lst = []
#     for i in value:
#         print(i)
#         lst.append(i.side)
#     return HttpResponse(lst)


# Задание №1 Семинар 3
# Изменяем задачу 8 из семинара 1 с выводом двух html страниц:
# главной и о себе.
# Перенесите вёрстку в шаблоны.
# Представления должны пробрасывать полезную информацию в
# шаблон через контекст.

#def base(request):
    #return render(request, 'iam/base.html')


def index(request):
    context = {'name': "Костя", 'lastname': "Иванов", 'age': 37}
    return render(request, 'iam/index.html', context=context)


def indextwo(request):
    return render(request, 'iam/indextwo.html')
