def f(n):  # n - индекс числа
    if n == 1 or n == 2:
        num = 1
        return num
    if n > 2:
        num = f(n - 1) + f(n - 2)
        return num  # num - полученное число


print(f(3))
