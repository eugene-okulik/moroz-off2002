# Задание 1
# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.

import random


salary = int(input('Введите значение переменной salary: '))
bonus = random.choice([True, False])
if bonus is True:
    result = salary + random.randint(100, 500)
else:
    result = salary
print(f'{salary}, {bonus} - ${result}')
