# Задача №31. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0=0, a1=1,
# ak=ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def fib(k):
#     if k<2:
#         return 1
#     return fib(k-1)+fib(k-2)
# a=int(input("Введите число: "))
# print(fib(a))



# Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# def zhurnal(a):
#     otsenky=[]
#     for i in range(a):
#         i=int(input("Введите оценку: "))
#         otsenky.append(i)
#     return otsenky

# def zamena (list1):
#     max_list1=max(list1)
#     min_list1=min(list1)
#     for i in range(len(list1)):
#         if list1[i]==max_list1:
#             list1[i]=min_list1
#     return list1

# a=int(input("Введите количество оценок от 1 до 5: "))
# fact=list(zhurnal(a))
# print(f"{a} -> ", end='')
# print(*fact)
# print(*zamena(fact))



# Задача №35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

# def prostoe(x):
#     if x<2:  #если число меньше 2-х то оно не простое 
#         return "no"
#     for i in range(2, x//2+1): #цикл пока доп.переменная не станет больше половины проверочного
#         if x % i==0: #если при делении проверочного числа на переменную получится 0, то оно имеет др. делитель кроме себя и непростое
#             return 'no'
#     return 'yes' #если цикл полностью отработал и не нашел делителя, то оно простое
# print(prostoe(int(input('Введите число для проверки: '))))


# Задача №37. Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в
# обратном порядке. Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def vyvod (x):
    a=input('Введите число: ')  
    if x==1:
        return a
    return vyvod(x-1) + a

print(vyvod(int(input("Введите число элементов: "))))


