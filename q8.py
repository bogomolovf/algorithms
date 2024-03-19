'''
Сортировка слиянием (Merge Sort) - это алгоритм сортировки, который 
использует принцип "разделяй и властвуй". Алгоритм разбивает массив 
на две половины, сортирует каждую половину рекурсивно, а затем сливает 
две отсортированные половины вместе, чтобы получить 
отсортированный массив.

Время работы сортировки слиянием зависит от размера массива и 
количества рекурсивных вызовов. Общая сложность алгоритма составляет
O(n log n), где n - размер массива.

Сортировка слиянием является одним из самых эффективных алгоритмов
сортировки для больших массивов, так как она гарантирует стабильность 
и не зависит от начального порядка элементов. Однако, она требует 
дополнительной памяти для хранения дополнительного массива, что может 
быть проблемой для больших массивов.
'''

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:

            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def merge_sort(nums):

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

random_list_of_nums = [120, 45, 68, 250, 176]
random_list_of_nums = merge_sort(random_list_of_nums)
print(random_list_of_nums)




