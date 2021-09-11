def f(n):
    if n == 1 or n == 2:
        num = 1
        return num
    if n > 2:
        num = f(n - 1) + f(n - 2)
        return num


print(f(3))
