"""
Потехин Павел Михайлович
15 вариант
КИ21-17/2б
"""
TEXT_INPUT = 'Введите число или Нажмите Enter для завершения программы: '
k = input(TEXT_INPUT)


def is_continue(k):
    """
    проверяет является ли строка числом
    """
    if not k:
        return False
    try:
        k = int(k)
    except ValueError:
        print("неправильно введено число, повторите попытку")
        return True
    tapper(k)
    return True


def tapper(k):
    """
    вычисляет значение формулы Таппера
    """
    for x in range(0, 106):
        for y in range(k, k + 17):
            if 1 / 2 < int((int(y // 17) // 2 ** (17 * x + y % 17)) % 2):
                print(1, end='')
            else:
                print(0, end='')
    print()


while is_continue(k):
    k = input(TEXT_INPUT)
