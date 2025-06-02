# Задание №3
# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции). Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение


def decorator(func):

    def wrapper(first, second):

        if first * second < 0:
            calc(first, second, '*')
            return func
        elif first == second:
            calc(first, second, '+')
            return func
        elif first > second:
            calc(first, second, '-')
            return func
        elif first < second:
            calc(first, second, '/')
            return func
    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        return 'incorrect operation'


first = int(input('Введите 1е число: '))
second = int(input('Введите 2е число: '))
calc(first, second)
