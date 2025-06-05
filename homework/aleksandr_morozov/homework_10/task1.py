# Задание №1
# Создайте универсальный декоратор, который можно будет применить к любой функции.
# Декоратор должен делать следующее: он должен распечатывать слово "finished" после выполнения декорированной функции.


def finish_me(func):

    def wrapper(*args):
        func(*args)
        print()
        print('finished')
        return func

    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
