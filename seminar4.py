# Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
# string1 = "a a a b c a a d c d d g"
# list1 = string1.split(" ")
# dict_count = {}
# for i in range(len(list1)):
#     if dict_count.get(list1[i]) is None:
#         dict_count[list1[i]] = 0
#     else:
#         dict_count[list1[i]] += 1
#         list1[i] = f"{list1[i]}_{dict_count[list1[i]]}"

# print(*list1)
# print(" ".join(list1)) #второй вариант вывода






# Задача №27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# input_str = ("She     sells sea shells on the sea shore "
#              "The shells that she sells are sea shells "
#              "I'm sure.So if she sells sea shells on the sea shore "
#              "I'm sure that the shells are sea shore shells")
# print(input_str)
# input_str = input_str.replace('.' ,' ')
# print(input_str)
# input_lst = input_str.split()
# print(input_lst)
# for i in range(len(input_lst)):
#     input_lst[i] = input_lst[i].lower()
# print(input_lst)
# print(len(set(input_lst)))
# print('*' * 15)
# res = len(set(i.lower() for i in input_str.replace('.' ,' ').split()))
# print(res)


