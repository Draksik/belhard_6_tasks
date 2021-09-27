"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(num: int):
    x = 0
    for y in str(num):
        x += int(y)
    return x


print(sum_of_numbers(888888))
