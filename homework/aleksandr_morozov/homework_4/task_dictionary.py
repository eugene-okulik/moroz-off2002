# Создание словаря

my_dict = {
    'my_tuple': (2, 5, 10, 43, 'super'),   # кортеж
    'my_list': ['one', 'two', 'three', 'four', 'five'],   # список
    'my_dict_inc': {'name': 'myname', 'surname': 'mysurname', 'age': 'myage', 'city': 'mycity',
                'country': 'mycountry'},   # словарь
    'my_set': {35, 11, 33, 11, 89, 0}   # множество
}
a = my_dict['my_tuple']
print('my_tuple last value:', a[-1])

b = my_dict['my_list']
b.append('six')
b.pop(1)
print('my_list:', b)

c = my_dict['my_dict_inc']
new_dict = {('i am a tuple',): 'yes i am'}
c.update(new_dict)
c.pop('city')
print('my_dict_inc:', c)

d = my_dict['my_set']
d.add(1)
d.remove(89)
print('my_set:', d)

print('my_dict:', my_dict)
