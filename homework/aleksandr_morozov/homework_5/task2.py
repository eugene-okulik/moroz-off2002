# Задание 2
# Допустим, какая-то программа возвращает результат своей работы в таком виде:
# результат операции: 42
# результат операции: 514
# результат работы программы: 9

text_result = 'результат работы программы: 9'
trigger_pos = text_result.index(':')
print('Trigger position:', trigger_pos)
value = int(text_result[trigger_pos + 2:])
print('Parsed value:', value)
calc_result = value + 10
print('Calculated result:', calc_result)
