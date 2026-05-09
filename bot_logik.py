import random

def gen_passssssss(length):


    tex = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    parol = ''

    for _ in range(length):
        t = random.choice(tex)
        parol += t
    return parol
def uwiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiikeiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii():
    keys = [
        # Буквы
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

        # Цифры
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',

        # Функциональные клавиши
        'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',

        # Модификаторы и системные клавиши
        'ctrl', 'alt', 'shift', 'win', 'cmd', 'menu', 'caps lock', 'num lock', 'scroll lock',

        # Клавиши навигации
        'tab', 'enter', 'backspace', 'space', 'escape',
        'home', 'end', 'page up', 'page down',
        'insert', 'delete',

        # Стрелки
        'left', 'up', 'right', 'down',

        # Блок цифровой клавиатуры
        'num_0', 'num_1', 'num_2', 'num_3', 'num_4',
        'num_5', 'num_6', 'num_7', 'num_8', 'num_9',
        'num_multiply', 'num_add', 'num_subtract', 'num_decimal', 'num_divide', 'num_enter',

        # Прочие символы (как они могут обозначаться в коде)
        '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
        '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', "'", '"',
        ',', '<', '.', '>', '/', '?'
    ]

    return random.choice(keys)