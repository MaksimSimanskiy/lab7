
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    c = int(input("Введите начало интервала "))
    d = int(input("Введите конец интервала "))

    print('Введите элементы в одну строку ')
    a = tuple(map(int, input().split()))
    if len(a) != 5:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    print('Максимальный элемент ' , max(a, key=abs))
    print('Индекс максимального элемента ' , a.index(max(a, key=abs)))
    k = (tuple(filter(lambda i: i > 0, a))[0])
    k = a.index(k)
    print('Сумма чисел после первого положительного числа',sum(a[k:]))
    print('Отсортированый кортеж',sorted(a,key = lambda x: d > x > c,reverse = True))
