import math


def to_fixed(obj, digits=0):  # фиксирует кол-во знаков после запятой
    return f"{obj:.{digits}f}"


def fib(n, k):  # выводит n-ый член последовательности
    x = (((k + math.sqrt(k ** 2 + 4)) / 2) ** n
         + ((k - math.sqrt(k ** 2 + 4)) / 2) ** n) / math.sqrt(5)
    return x


def golden_rat():  # находит золотое сеч по формуле
    return to_fixed((math.sqrt(5) + 1) / 2, 5)


def del_(a, b):  # находит отношение м/у членами послед.
    return to_fixed(a / b, 5)


def compare(otn, fi):  # сравнивает отношение членов послед. с золотым сечением
    if otn > fi:
        return 'отношение членов последовательности Фибоначчи болше золотого сечения'
    elif otn == fi:
        return 'отношение членов последовательности Фибоначчи равно золотому сечению'
    else:
        return 'отношение членов последовательности Фибоначчи меньше золотого сечения'


print(fib(2, 1), '\n',
      del_(fib(2, 1), fib(1, 1)), '\n',
      compare(del_(fib(2, 1), fib(1, 1)), golden_rat()))
