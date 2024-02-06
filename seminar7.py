# Задача №47. У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.



# values = [1, 23, 42, 'asdfg']
# transformation = lambda x: x
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#  print('ok')
# else:
#  print('fail')

# print(values)
# print(transformed_values)
# print(' '.join(map(str, transformed_values))) #метод join преобразует только значения строки, но не интовые, поэтому ф-цией map пробегаем по всем элементам списка и предобразуем ф-цией str в строку





# Задача №49. Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Резуь кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждаяя орбита представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна

# def find_farthest_orbit(list_of_orbits):
#     S=list(map(lambda x: x[0]*x[1]*3.14 if x[0]!=x[1] else 0, list_of_orbits))
#     max_orbits=list_of_orbits[S.index(max(S))]
#     return max_orbits
    
    
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))




# Задача №51. Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его
# характеристику.

def same_by(characteristic, objects):
    if len(objects) == 0: return True
    temp = characteristic(objects[0])
    list_1 = list(map(lambda x: characteristic(x) == temp, objects))
    # print(list_1)
    print(all(list_1))

values = [0, 2, 1, 6]
simple=lambda x: x % 2 == 0
same_by(simple, values)

