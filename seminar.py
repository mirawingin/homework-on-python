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
import math

def find_farthest_orbit(list_of_orbits):
    farthest_orbit = max(list_of_orbits, key=lambda orbit: math.pi * orbit[0] * orbit[1] if orbit[0] != orbit[1] else -1)
    return farthest_orbit

# Пример использования функции
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (8, 8)]
print(*find_farthest_orbit(orbits))






