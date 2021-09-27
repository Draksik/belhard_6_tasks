"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(listok: list):
    new_list = []
    for item in listok:
        if item in new_list:
            print("Yes")
        else:
            new_list.append(item)
            print("No")


testik = [1, 2, 3, 6, 5, 1, 2, 3]
yes_or_no(testik)
