# Задание 2
# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число


import sys


sys.set_int_max_str_digits(1000000)


def progression(limit=100):
    num1 = 0
    num2 = 1
    num3 = 1
    count = 1
    while count < limit:
        yield num3
        num3 = num2 + num1
        num1 = num2
        num2 = num3
        count += 1


counter = 1
for number in progression(100001):
    if counter == 5:
        print(number)
    elif counter == 200:
        print(number)
    elif counter == 1000:
        print(number)
    elif counter == 100000:
        print(number)
    counter += 1
