"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").
Проверить, что все аргументы целые можно с помощью функции all:
https://pyneng.readthedocs.io/ru/latest/book/10_useful_functions/all_any.html

Если все аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):
    if all(type(i) is int for i in args):
        summa = {"args_sum": sum(args)}
    else:
        raise TypeError("Все позиционные аргументы должны быть целыми")
    if all(type(value) is str for value in kwargs.values()):
        kwargs_max_len = {"kwargs_max_len": max([len(value) for value in kwargs.values()])}
    else:
        raise TypeError("Все аргументы - ключевые слова должны быть строками")
    summa.update(kwargs_max_len)
    return summa
