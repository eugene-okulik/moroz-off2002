# Задание 2 - "FuzzBuzz"

for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print('FuzzBuzz')
        else:
            print('Fuzz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
