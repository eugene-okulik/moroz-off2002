# Букет цветов с сортировкой и поиском по параметру объектов


class Flowers:

    def __init__(self, freshness, colour):
        self.freshness = freshness
        self.colour = colour


class Rose(Flowers):
    lifetime = 10
    stemlength = 50
    price = 200

    def __str__(self):
        return (f'\n{self.__class__.__name__}, свежесть: {self.freshness}, цвет: {self.colour}, цена: {self.price}, '
                f'длина стебля: {self.stemlength}, время жизни: {self.lifetime}')

    def __repr__(self):
        return (f'\n{self.__class__.__name__}, свежесть: {self.freshness}, цвет: {self.colour}, цена: {self.price}, '
                f'длина стебля: {self.stemlength}, время жизни: {self.lifetime}')


class Tulip(Flowers):
    lifetime = 5
    stemlength = 30
    price = 100

    def __str__(self):
        return (f'\n{self.__class__.__name__}, свежесть: {self.freshness}, цвет: {self.colour}, цена: {self.price}, '
                f'длина стебля: {self.stemlength}, время жизни: {self.lifetime}')

    def __repr__(self):
        return (f'\n{self.__class__.__name__}, свежесть: {self.freshness}, цвет: {self.colour}, цена: {self.price}, '
                f'длина стебля: {self.stemlength}, время жизни: {self.lifetime}')


class Chamomile(Flowers):
    lifetime = 7
    stemlength = 20
    price = 50

    def __str__(self):
        return (f'\n{self.__class__.__name__}, свежесть: {self.freshness}, цвет: {self.colour}, цена: {self.price}, '
                f'длина стебля: {self.stemlength}, время жизни: {self.lifetime}')

    def __repr__(self):
        return (f'\n{self.__class__.__name__}, свежесть: {self.freshness}, цвет: {self.colour}, цена: {self.price}, '
                f'длина стебля: {self.stemlength}, время жизни: {self.lifetime}')


class Bouquet:

    def __init__(self, *flowers):
        self.list = [*flowers]

    def avg_lifetime(self):
        sum_lifetime = sum(flower.lifetime for flower in self.list)
        avg_lifetime = sum_lifetime / len(self.list)
        return avg_lifetime

    def sort_by_colour(self):
        sorted_list = sorted(self.list, key=lambda x: x.colour)
        return sorted_list

    def sort_by_freshness(self):
        sorted_list = sorted(self.list, key=lambda x: x.freshness)
        return sorted_list

    def sort_by_price(self):
        sorted_list = sorted(self.list, key=lambda x: x.price)
        return sorted_list

    def sort_by_stemlength(self):
        sorted_list = sorted(self.list, key=lambda x: x.stemlength)
        return sorted_list

    def filter_by_lifetime(self, lifetime):
        found_list = list(filter(lambda x: x.lifetime == lifetime, self.list))
        if found_list:
            return found_list
        else:
            print('Cовпадений не найдено')
            return None


flower1 = Rose('good', "red")
flower2 = Tulip('normal', 'yellow')
flower3 = Chamomile('very good', 'white')
flower4 = Rose('good', "white")
flower5 = Tulip('bad', "violet")

bouquet1 = Bouquet(flower1, flower2, flower5, flower4, flower3)
print(bouquet1.avg_lifetime())
print(bouquet1.list)
print(bouquet1.sort_by_colour())
print(bouquet1.sort_by_freshness())
print(bouquet1.sort_by_price())
print(bouquet1.sort_by_stemlength())
print(bouquet1.filter_by_lifetime(5))
