from random import choice, random, randint
from .models import Coin


# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello world!!!')


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


def base(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Мой первый Django-сайт</title>
        </head>
        <body>
            <h1>Добро пожаловать на мой первый Django-сайт!</h1>

            <h2>О сайте</h2>
            <p>Этот сайт разработан с использованием Django, мощного фреймворка для создания веб-приложений на языке Python.</p>

            <h2>Обо мне</h2>
            <p>Настя. Просто Настя.</p>

            <footer>
                <p>Здесь могла быть ваша реклама</p>
            </footer>
        </body>
    </html>
    """
    #logger.info(f'посещение страницы base в: {datetime.now()}')
    return HttpResponse(html)


def about(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Обо мне</title>
        </head>
        <body>
            <header>
                <h1>Доброго дня! Сегодня отличный день!</h1>
            </header>

            <main>
                <section>
                    <h2>Не хотелось бы спорить, но вот доводы:</h2>
                    <ul>
                        <li>Солнце светит</li>
                        <li>Вода течет</li>
                        <li>Ветер дует</li>
                        <li>Огонь греет</li>
                    </ul>
                </section>

            <footer>
                <p>Здесь снова могла бы быть ваша реклама</p>
            </footer>
        </body>
    </html>
    """
    #logger.info(f'посещение страницы about в: {datetime.now()}')
    return HttpResponse(html)
