# Задание 4. List comprehension


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.split()
goods = new_list[0::2]
print(goods)
prices = [int(p[:-1]) for p in new_list[1::2]]
print(prices)
new_dict = dict(zip(goods, prices))
print(new_dict)
