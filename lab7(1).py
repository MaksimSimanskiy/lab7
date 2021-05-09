#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
b = ()
print('Введите элементы кортежа в одну строку ')
a = tuple(map(int, input().split()))
if len(a) != 10:
    print("Неверный размер кортежа", file=sys.stderr)
    exit(1)

b = tuple(filter(lambda x: 20 > x > 2 and x % 8 == 0, a))
print('Список А = {}\nВыбраные элементы = {} \nКоличество элементов  = {} \nСумма = {}'.format(a, b, len(b), sum(b)))
