'''
Статический массив - массив из элементов, на который нужно
изначально выделить память.

Динамический массив - массив, размер которого может
изменяться во время выполнения программы.

Время добавления: O(n) - в худшем (ĸогда надо перенести все элементы
из теĸущего массива во вдвое больший), O(1) - в лучшем.
'''
static_array = [1, 2, 3]
dynamic_array = []
dynamic_array.append(1)
dynamic_array.append(2)
dynamic_array.append(3)