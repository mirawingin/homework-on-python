#######################################################################################
# задача № 45 . два различных натуральных числа n  и m называются дружественными,
# если сумма  делителей числа  n (включая 1, но исключая само n) ровна числу m 
# и наоборот. Например, 220 и  284 - дружественные числа. По данному числу k 
# выведите  все пары дружественных чисел, каждое из которых не превосходит k. 
# программа получает на вход одно натуральное число k, не превосходящее 10 в 
# пятой степени, программа должна вывести  все пары  дружественных чисел, 
# каждое из которых не превосходит k. пары необходимо выводить по одной в строке,
# разделяя пробелами. Каждая пара должна быть выведена только один раз 
# ( перестановка чисел новую пару не дает).  Ввод -  300   Вывод  220   284
# ##########################################################
############    решение  #############################3##
##########################################################
# Функция для вычисления суммы всех делителей числа
"""def сумма_делителей(n):
    сумма = 0
    for i in range(1, n):
        if n % i == 0:
            сумма += i
    return сумма
# # def сумма_делителей(n):: Это объявление функции с именем сумма_делителей, которая принимает один аргумент n, 
# # представляющий число, для которого мы хотим найти сумму его делителей.
# # сумма = 0: Мы инициализируем переменную сумма с нулевым значением. Эта переменная 
# # будет использоваться для хранения суммы делителей числа n.for i in range(1, n):: 
# # Мы используем цикл for для перебора всех чисел от 1 до n - 1. Мы начинаем с 1, 
# # потому что делители числа исключают само число n.
# # if n % i == 0:: Мы проверяем, является ли i делителем числа n.
# # Если остаток от деления числа n на i равен нулю, то i является делителем числа n.
# # сумма += i: Если i является делителем числа n, мы добавляем его к переменной сумма.
# # return сумма: В конце функции мы возвращаем сумму всех делителей числа n.
# # Функция для нахождения всех дружественных чисел, где первое число не превышает 
# # введенное пользователем число
def дружественные_числа(k):
    дружественные = []
    for n in range(1, k + 1):
        m = сумма_делителей(n)
        if m > n:  # Проверяем, что сумма делителей больше числа n
            if сумма_делителей(m) == n and m <= k:  # Проверяем условие дружественных чисел и что второе 
                                                     #число не превышает k
                дружественные.append((n, m))
    return дружественные
# # def дружественные_числа(k):: Это объявление функции дружественные_числа, 
# # которая принимает один аргумент k, представляющий число, до которого мы хотим 
# # найти дружественные числа.дружественные = []: Мы инициализируем пустой список 
# # дружественные, в который будем добавлять пары дружественных чисел.
# # for n in range(1, k + 1):: Мы используем цикл for для перебора всех чисел от 1 до k. 
# # Мы включаем k в диапазон, потому что мы хотим искать дружественные числа включая 
# # k.m = сумма_делителей(n): Мы находим сумму делителей числа n, используя функцию сумма_делителей.
# # if m > n:: Мы проверяем, что сумма делителей числа n больше самого числа n. Это
# # позволяет нам исключить числа, которые не могут быть дружественными.
# # if сумма_делителей(m) == n and m <= k:: Мы проверяем, что сумма делителей числа m равна числу n,
# # и что m не превышает число k. дружественные.append((n, m)): Если числа n и m удовлетворяют
# # условиям дружественных чисел, мы добавляем их в список дружественные в виде кортежа (n, m).
# # return дружественные: В конце функции мы возвращаем список всех дружественных чисел.
# # Получаем входные данные от пользователя

k = int(input("Введите число k: "))
## Находим все дружественные числа, где первое число не превышает k
результат = дружественные_числа(k)
## Выводим результат
print("Пары дружественных чисел, где первое число не превышает", k, ":")
for пара in результат:
    print(пара[0], пара[1])
k = int(input("Введите число k: "))
    # # Мы запрашиваем у пользователя ввод числа k, до которого 
    # #  мы хотим найти дружественные числа, и преобразуем его в целое число.
    # # pезультат = дружественные_числа(k): Мы вызываем функцию дружественные_числа с аргументом k и 
    # #  сохраняем результат в переменную результат.
print("Пары дружественных чисел, где первое число не превышает", k, ":") """#Мы выводим заголовок,
  #   ####указывающий на то, что следующие пары дружественных чисел имеют первое число, которое не превышает k.
  # # for пара in результат:: Мы используем цикл for для перебора всех пар дружественных чисел в результат.
  # # print(пара[0], пара[1]): Мы выводим каждую пару дружественных чисел. пара[0] представляет первое число,
  # # а пара[1] представляет второе число в паре.
##########################################################################################################
##########################################################################################################
##########################################################################################################
# задача № 49
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

#####################################################################
# Нам нужно найти орбиту, по которой вращается самая далекая планета, при условии, что это эллипс, а не круг.
# Алгоритм решения:
# Мы можем использовать формулу для вычисления площади эллипса: S=π⋅a⋅b, где a и b - полуоси эллипса.
# Нам нужно найти орбиту с наибольшей площадью. Для этого мы будем вычислять площадь каждой орбиты и выбирать 
# орбиту с максимальной площадью. Однако нам нужно игнорировать круговые орбиты, так как они не являются эллипсами.
# Для этого мы будем проверять, является ли орбита эллипсом или кругом.
# Реализация:
# Мы создаем функцию find_farthest_orbit, которая принимает список орбит list_of_orbits.
# Для каждой орбиты мы вычисляем площадь и используем условное выражение, чтобы вернуть -1, если орбита является кругом.
# Мы используем функцию max для поиска орбиты с максимальной площадью, игнорируя круговые орбиты.
# Наконец, мы возвращаем найденную орбиту.
# Таким образом, мы пришли к решению задачи, которое позволяет нам найти эллиптическую орбиту, по которой вращается самая далекая планета.
###################################################################
# import math

# def find_farthest_orbit(list_of_orbits):
#     farthest_orbit = max(list_of_orbits, key=lambda orbit: math.pi * orbit[0] * orbit[1] if orbit[0] != orbit[1] else -1)
#     return farthest_orbit

# # Пример использования функции
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (8, 8)]
# print(*find_farthest_orbit(orbits))
#######################################################################
# import math: 
# Эта строка импортирует модуль math, который предоставляет математические функции и константы, такие как pi (число пи).
# def find_farthest_orbit(list_of_orbits):: 
# Это объявление функции find_farthest_orbit, которая принимает один аргумент list_of_orbits, представляющий список орбит планет.
# farthest_orbit = max(list_of_orbits, key=lambda orbit: math.pi * orbit[0] * orbit[1] if orbit[0] != orbit[1] else -1):
# Эта строка находит орбиту с наибольшей площадью в списке list_of_orbits, игнорируя круговые орбиты. 
# Функция max принимает список орбит list_of_orbits и ключевую функцию key, которая применяется к каждой орбите для вычисления значения, 
# по которому будет производиться сравнение. В данном случае используется анонимная функция lambda, которая вычисляет 
# площадь орбиты по формуле S=π⋅a⋅b, 
# где orbit[0] и orbit[1] представляют длины полуосей эллипса орбиты. 
# Условное выражение if orbit[0] != orbit[1] else -1 проверяет, является ли орбита эллипсом или кругом. 
# Если орбита является кругом, то возвращается -1, чтобы эта орбита была игнорирована в функции max.
# return farthest_orbit: Эта строка возвращает найденную орбиту с наибольшей площадью из функции find_farthest_orbit.
# # Пример использования функции
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (8, 8)]
# print(*find_farthest_orbit(orbits))
# Эти строки демонстрируют использование функции find_farthest_orbit на примере. Мы создаем список orbits, содержащий орбиты планет,
# а затем вызываем функцию find_farthest_orbit с этим списком и выводим результат. 
# Функция print с аргументом *find_farthest_orbit(orbits) распаковывает кортеж, 
# возвращаемый функцией find_farthest_orbit, и выводит его содержимое.
#############################################################################################
#############################################################################################
#############################################################################################
# Задача №51.
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
# Понимание задачи:
# Нам нужно написать функцию same_by, которая будет проверять, имеют ли все объекты одинаковое значение некоторой характеристики.
# Функция same_by должна принимать два аргумента: characteristic (характеристика) и objects (список объектов).
# Для пустого списка объектов функция должна возвращать True.
# Алгоритм решения:

# Мы будем использовать функцию map, чтобы применить характеристику ко всем объектам.
# Затем мы сравним все значения характеристики. Если они все одинаковы, вернем True, иначе - False.
# Реализация:

# Создадим функцию same_by, которая принимает характеристику и список объектов.
# Используем функцию map для вычисления характеристики для каждого объекта.
# Преобразуем результаты map в список значений характеристики.
# Проверим, все ли значения в списке одинаковы. Если да, вернем True, иначе - False.
# Вот как это выглядит в коде:
###############################################################################################
def same_by(characteristic, objects):
    characteristics = list(map(characteristic, objects))
    return len(set(characteristics)) == 1 or len(objects) == 0

# Пример использования функции
values = [0, 2, 10, 7, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
#################################################################################################
# В этом коде мы используем lambda функцию, которая вычисляет остаток от деления на 2 для каждого 
# элемента в списке values. Функция same_by проверяет, все ли значения характеристики 
# (остатков от деления на 2) одинаковы. Если да, то выводится 'same', иначе - 'different'.










