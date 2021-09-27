"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(num):
    if num % 2 == 0:
        num = num / 2
        return check_number(num)
    elif num == 2 or num == 1:
        return True
    else:
        return False


odd = check_number(3)
print(odd)
