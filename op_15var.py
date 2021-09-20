"""
Потехин Павел Михайлович
15 вариант
КИ21-17/2б
"""
import pygame as py
from pygame import event


screen = py.display.set_mode([1024, 256])


VERTICAL = 256
HORIZONTAL = 1024


def address_(x, y):
    py.draw.rect(screen, (255, 255, 255), (x, y, 8, 8))


def is_continue(k):
    try:
        k = int(k)
    except ValueError:
        print("неправильно введено число, повторите попытку")
        return True
    if (k % 17) != 0:
        print('напишите число, кратное 17. Остаток от деления :', k % 17)
        return True
    if k < 0:
        k *= -1
    tapper(k)
    return False


def tapper(k):
    """
    вычисляет значение формулы Таппера
    """
    for x in range(0, 106):
        for y in range(k, k + 17):
            if 1 / 2 < int((y // 17 // 2 ** (17 * x + y % 17)) % 2):
                print(1, end='')
                address_(x * 8, VERTICAL - 8 - (y % 17) * 8)
            else:
                print(0, end='')
    print()


const = 1
while const:
    TEXT_INPUT = 'Введите число или Нажмите q для завершения программы: '
    k = input(TEXT_INPUT)
    while is_continue(k):
        k = input(TEXT_INPUT)
    button = 1
    while button:
        py.display.update()
        for press in py.event.get():
            if press.type == py.KEYDOWN:
                if press.key == py.K_ESCAPE:
                    button = 0
                if press.key == py.K_q:
                    py.quit()
                    button = 0
                    const = 0               
    screen.fill((0, 0, 0))




    













    104716252351532169455825580758668753734889024636588709449126952151161878058639583177284778741648375052651374679791545822918838546439205198867386915797298611598946270817073358399117099732385463108273046292173063061011752270727663947895205552230870470422012914433085384539720195938096808340642311741418630834682254361917233039291210933728609174017293571507783591664739133206426660659112206901901960297310966318812632552011397602733095381745743493137533408396078540164072293731182961770430624088195072