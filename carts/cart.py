#!/usr/bin/python
# - *- coding: utf- 8 - *-

from decimal import Decimal
from django.conf import settings
from alldetail.models import Articles
from cupons.models import Cupon


class Cart(object):
    def __init__(self, request):
        # Инициализация корзины пользователя
        self.session = request.session
        self.cupon_id = self.session.get('cupon_id')
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем корзину пользователя в сессию
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # Добавление товара в корзину пользователя или обновление количеста товара
    def add(self, article, quantity=1, update_quantity=False):
        article_id = str(article.id)
        if article_id not in self.cart:
            self.cart[article_id] = {'quantity': 0,
                                     'price': str(article.price)}
        if update_quantity:
            self.cart[article_id]['quantity'] = quantity
        else:
            self.cart[article_id]['quantity'] += quantity
        self.save()

    # Сохранение данных в сессию
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # Указываем, что сессия изменена
        self.session.modified = True

    def remove(self, article):
        article_id = str(article.id)
        if article_id in self.cart:
            del self.cart[article_id]
            self.save()

    # Итерация по товарам
    def __iter__(self):
        article_ids = self.cart.keys()
        articles = Articles.objects.filter(id__in=article_ids)
        for article in articles:
            self.cart[str(article.id)]['article'] = article

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    # Количество товаров
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    @property
    def cupon(self):
        if self.cupon_id:
            return Cupon.objects.get(id=self.cupon_id)
        return None

    def get_discount(self):
        if self.cupon:
            return (self.cupon.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()     
