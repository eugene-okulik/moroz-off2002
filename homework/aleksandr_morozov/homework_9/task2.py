# Map, filter
# С помощью функции map или filter создайте из этого списка новый список с жаркими днями. Будем считать жарким всё,
# что выше 28.
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.


temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30,
                32, 30, 28, 24, 23]

warm_days = filter(lambda x: x > 28, temperatures)
warm_days_list = list(warm_days)
average = sum(warm_days_list) / len(warm_days_list)
print(warm_days_list)
print(max(warm_days_list))
print(min(warm_days_list))
print(round(average, 2))
