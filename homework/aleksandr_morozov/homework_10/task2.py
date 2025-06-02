# Задание №2
# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция


def repeat_me(func):

    def wrapper(*args, count):
        x = 0
        while x < count:
            func(*args)
            x = x + 1
        return func

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
