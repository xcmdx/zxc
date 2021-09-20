n, m = input().split()
n, m = int(n), int(m)


def flavius(n, m): #n - кол-во солдат m - шаг
    if n > 1:
        return (flavius(n - 1, m) + m - 1) % n + 1
    else:
        return 1


print(flavius(n, m))