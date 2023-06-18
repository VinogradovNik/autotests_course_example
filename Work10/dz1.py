# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

from random import randint
import string
import random
def generate_random_name():
    letters = string.ascii_lowercase
    two_words = ''
    for i in range(2):
        random_number = randint(1, 15)
        word = ''.join(random.choice(letters) for i in range(random_number))
        two_words += word + ' '
    return two_words
gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))