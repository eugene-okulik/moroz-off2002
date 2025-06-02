# Задание №2
# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция
# через передачу аргумента во внешний слой декоратора.


def repeat_me(count):

    def repeat_me_inc(func):

        def wrapper(*args):
            x = 0
            while x < count:
                func(*args)
                x = x + 1

        return wrapper

    return repeat_me_inc


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
