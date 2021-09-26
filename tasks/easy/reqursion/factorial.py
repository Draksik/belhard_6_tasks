"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент

5! = 1 * 2 * 3 * 4 * 5 = 125
"""


def factorial(n):
    if n < 1:
        raise ValueError
    if n == 1:
        return n
    else:
        return factorial(n - 1) * n


print(factorial(5))
