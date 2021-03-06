import random, math

__author__ = 'Чернышев Павел'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

print('Задача #1')

var = str(random.randrange(0, 10000))
print(f'Произвольное число от 0 до 10000: {var}')

cnt = 0
max = 0
while cnt < len(var):
    if max < int(var[cnt]):
        max = int(var[cnt])
    cnt += 1
print(f'Наибольшая цифра в числе: {max}')

print(' ')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

# ! А если пользователь ввел строковую переменную? Какие операции над числами можно проводить?
# ! Например: А=123 B='Hello world!'
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print('Задача #2')

list = [ input('Введите переменную A: ') ]
list.append(input('Введите переменную B: '))
print(f'А = {list[0]}, B = {list[1]}')

list.reverse()

print(f'Меняем местами, теперь A = {list[0]}, B = {list[1]}')

print(' ')
# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print('Задача #3')
print('Будем решать уравнение А*x2 + B*x + C = 0')
A = int(input('Введите А: '))
B = int(input('Введите B: '))
C = int(input('Введите C: '))
print(f'Уравнение {A}*x2 + {B}*x + {C} = 0')

if A == 0:
    X = -C / B
    print(f'Решение X = {X}')
else:
    D = B*B - 4*A*C

    if D < 0:
        print('Слишком сложно')
    elif D == 0:
        X = -B / (2 * A)
        print(f'Решение X = {X}')
    else:
        X1 = (-B - math.sqrt(D)) / (2 * A)
        X2 = (-B + math.sqrt(D)) / (2 * A)
        print(f'Решение X1 = {X1}, X2 = {X2}')
