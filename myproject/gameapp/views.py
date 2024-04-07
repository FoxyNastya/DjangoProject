from random import choice, random, randint
from .models import Coin
from .forms import GameCoinForm


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


#def index(request):
 #   return HttpResponse('Hello world!!!')


def coin(request, size: int = 1):
    # return HttpResponse([choice(['орел', 'решка']) for i in range(size)
    lst = [choice(['орел', 'решка']) for i in range(size)]
    print(lst)
    return render(request, 'gameapp/coin.html', {'lst': lst})

def dice(request):
    pass


def game_choice(requests):
    if requests.method == 'POST':
        form = GameCoinForm(requests.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            size = form.cleaned_data['size']
            if game == 'coin':
                return coin(requests, size)
    else:
        form = GameCoinForm()
    return render(requests, 'gameapp/game.html', {'form': form})


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

#
# Задание №1
# Доработаем задачу про броски монеты, игральной кости и
# случайного числа.
# Создайте форму, которая предлагает выбрать: монета, кости,
# числа.
# Второе поле предлагает указать количество попыток от 1 до 64.

# Задание №2
# Доработаем задачу 1.
# Создайте представление, которое выводит форму выбора.
# В зависимости от переданных значений представление
# вызывает одно из трёх представлений, созданных на
# прошлом семинаре (если данные прошли проверку, конечно
# же).
