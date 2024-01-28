# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах. На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо
# Пример На входе:
# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# Выход: 3 5

# var1 = '5 4'
# var2 = '5 6 7 8'
# var3 = '6 7 8 9'
# v2=set(var2.split())
# v3=set(var3.split())
# v4=v2.intersection(v3)
# list_1=list(v4)

# for j in range(len(list_1)-1):
#     min=j
#     for i in range(j+1,(len(list_1))):
#         if list_1[i]<list_1[min]:
#             min=i
    
#     list_1[j], list_1[min] = list_1[min], list_1[j]
    
# print(*list_1)





# В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, и кусты черники высажены по окружности грядки.
# Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте.
# Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.
# В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом,
# и он может выбирать, с какого куста начать сбор ягод.
# Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий модуль за один заход,
# находясь перед некоторым кустом грядки.
# Входные данные:
# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.
# Выходные данные:
# Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, находясь перед некоторым
# кустом грядки.
# Пример использования На входе:
# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# На выходе: 19

# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# max=arr[0]+arr[-1]+arr[-2]
# for i in range(len(arr)):
#     a=arr[i]
#     b=arr[i-1]
#     c=arr[i-2]
#     sum=a+b+c
#     if sum>max:
#         max=sum
# print(max)


