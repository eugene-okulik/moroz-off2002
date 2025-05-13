# Задание №1. Напишите программу, которая добавляет ‘ing’ в конец слов

text_origin = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis '
               'vitae semper at, dignissim vitae libero')

words = text_origin.split()
text_new = []
for word in words:
    if word.endswith(','):
        word = word.replace(',', 'ing,')
    elif word.endswith('.'):
        word = word.replace('.', 'ing.')
    else:
        word = word + 'ing'
    text_new.append(word)

print(' '.join(text_new))
