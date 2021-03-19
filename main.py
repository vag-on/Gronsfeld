import os

A = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ ' * 2  # алфавит


def f(text, k, op):
    k *= len(text) // len(k) + 1
    text = text.upper()
    return ''.join([A[A.index(j) + int(k[i]) * op] for i, j in enumerate(text)])


def encrypt(message, key):
    return f(message, key, 1)


def decrypt(ciphertext, key):
    return f(ciphertext, key, -1)


print('Программа шифрования и дешифрования методом Гронсфельда\n')
mes = ''
key = ''
z = 0
while z < 1:
    print('Выберите функцию:\n1. Зашифровать\n2. Дешифровать\n3. Выход')
    m = int(input())
    if m == 1:
        print('Введите сообщение: ')
        mes = input()
        print('Введите ключ: ')
        key = input()
        print('Результат шифрования с ключом ' + key + ':')
        print(encrypt(mes, key) + '\n')
    elif m == 2:
        print('Введите шифр: ')
        mes = input()
        print('Введите ключ: ')
        key = input()
        print('Результат дешифрования с ключом ' + key + ':')
        print(decrypt(mes, key) + '\n')
    elif m == 3:
        z = 1
    else:
        print('Неверный ответ')

