# Задание 3


a = 'результат операции: 42'
b = 'результат операции: 54'
c = 'результат работы программы: 209'
d = 'результат: 2'


def calc(text_result):
    trigger_pos = text_result.index(':')
    value = int(text_result[trigger_pos + 2:])
    calc_result = value + 10
    return calc_result


print(calc(a))
print(calc(b))
print(calc(c))
print(calc(d))
