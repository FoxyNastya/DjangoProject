# Задание
# Создайте три модели Django: клиент, товар и заказ.
# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.
## Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента
## Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
## Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа
#
# Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой ба

from django.db import models

# Create your models here.


class Client(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    phonenum = models.IntegerField(null=False)
    address = models.CharField(max_length=100, null=False)
    regdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.fullname}, emai: {self.email}'


class Product(models.Model):
    productitem = models.CharField(max_length=50, null=False)
    productdescription = models.TextField(null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    count = models.IntegerField(default=0)
    adddate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.productitem}, количество: {self.count}, цена: {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    ordersum = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    dateorder = models.DateTimeField(auto_now_add=True)






