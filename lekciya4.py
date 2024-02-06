# from random import randint

# # n=int(input('Введите число элементов: '))
# # spisok=[randint(0, 20) for i in range(n)]
# # print(*spisok)


# # spisoc2=[(spisok[x], spisok[x]**2) for x in range(len(spisok)) if spisok[x]%2==0]
# # print(spisoc2)


# list_1=[x for x in range(1, 20)]
# print(list_1)

# list_1=list(map(lambda x: x+10, list_1))
# print(list_1)

# # Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
# # используется пробел. Этот набор чисел будет считан в качестве строки. Как
# # превратить list строк в list чисел?

# data = '1 2 3 5 8 15 23 38'.split()
# data = list(map(int,input().split()))
# print(data)



# #функция фильтер
# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res) # [0, 2, 4, 6, 8]


# #Функция zip
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14),('user5', 7)]

# #Функция zip () пробегает по минимальному входящему набору:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

# #Функция enumerate()
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]



#РАБОТА С ФАЙЛАМИ

# # #Режим a:
# words=['привет', "! ", "Как ", "тебя ", "зовут", "? "]
# data=open('file3.txt', 'a')
# data.writelines(words)    #writelines указаыввает, что мы хотим записать данные из списка words
# data.write('меня зовут Олеся') #write - записывает строку, а не список
# data.close()     #файл всегда не забываем закрыть после открытия

# #Режим w:
# with open('file.txt', 'w') as data:
#     data.writelines('line 1\n')
#     data.write('line 2\n') #\n - отсутуп

# #Режим r
path = 'file3.txt'
data = open(path, 'r')
# for line in data:
#     print(line)
k = data.readlines()
print(*k)

data.close()

