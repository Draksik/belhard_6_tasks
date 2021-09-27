"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming language'


def count_char(STR_VAL):
    new_dict = {}
    for i in STR_VAL:
        new_dict.setdefault(i, 0)
        new_dict[i] += 1
    return new_dict


print(count_char(STR_VAL))
