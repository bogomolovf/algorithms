'''
Дан отсортированный массив чисел и искомый элемент. Необходимо 
найти индекс этого элемента в массиве (если элемент найден), 
либо вернуть значение -1(если элемент не найден)

Бинарный поиск имеет логарифмическую сложность 
O(log n), где n - количество элементов в массиве. 
Это означает, что время выполнения алгоритма растет
медленнее, чем линейно, с увеличением размера массива. Таким образом, 
бинарный поиск является эффективным алгоритмом для поиска элемента 
в отсортированном массиве.

Три вида бинарного поиска: обычный, левый и правый. Раличие в том, что 
левый бинарный поиск всегда возвращает индекс самого левого вхождения 
искомого элемента, а правый - правого. Обычный же бинарный поиск может 
вернуть индекс любого из дубликатов.
'''

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def left_binary_search(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left if left < len(arr) and arr[left] == target else -1


def right_binary_search(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return right - 1 if right > 0 and arr[right - 1] == target else -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
targ = 15
print(left_binary_search(arr, targ))