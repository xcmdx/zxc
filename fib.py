def fib(n):
    if n == 1 or n == 2:
        num = 1
        return num
    if n > 2:
        num = fib(n - 1) + fib(n - 2)
        return num


print(fib(3))
