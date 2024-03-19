'''
1.Bubble Sort
Лучшее время - O(n), если массив уже отсортирован.

Среднее время - O(n^2) , думаю очевидно, что мы n-1 раз запускаем цикл 
сравнения двух соседних элементов во всём массиве, поэтому получается
что-то типо (n-1)*n, поэтому такая асимптотика.

Худшее время - O(n^2) - аналогично среднему.

Память - O(1)

2.Insertion Sort
Лучшее время - O(n) - уже отсортирован.

Среднее время - O(n^2) - для каждого из элементов мы ищем место в уже
упорядоченный массив(сравнение с уже отсортированными эл-ми) - 
поэтому в среднем будет n^2.

Худшее время - O(n^2) - худшим случаем является массив, отсортированный в
порядке, обратном нужному. При этом каждый новый элемент сравнивается со 
всеми в отсортированной последовательности.

Память - O(1)

3.Selection Sort
Лучшее время - O(n^2) - для каждого элемента в неотсортированных ищется
максимум и меняется с последним в неотсортированной части =>
будет n+(n-1)...+1 = n*(n+1)/2 “дейстивий” => асимптота O(n^2)

Среднее время - O(n^2)

Худшее время - O(n^2)

Память - O(1)
'''

#Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

#Heap Sort
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

arr = [64, 25, 12, 22, 11]
print("Bubble Sort:", bubble_sort(arr.copy()))
print("Insertion Sort:", insertion_sort(arr.copy()))
print("Selection Sort:", selection_sort(arr.copy()))
print("Heap Sort:", heap_sort(arr.copy()))


