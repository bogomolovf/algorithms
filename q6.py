'''
Двоичная куча – это структура данных, представляющая собой полное двоичное
дерево, в котором каждый узел имеет значение не меньше (для кучи минимумов) или
не больше (для кучи максимумов) значений его потомков.

Построение двоичной кучи происходит путем добавления элементов по одному в
конец массива и последующего выполнения операции просеивания вверх (для
добавленного элемента) или вниз (если элемент стал корневым после просеивания
вверх).

Добавление элемента в кучу минимумов происходит следующим образом: 
элемент добавляется в конец массива и выполняется операция 
просеивания вверх. Эта операция заключается в том, что элемент 
сравнивается с его родителем. Если значение элемента меньше значения 
родителя, то элемент меняется местами с родителем и продолжается 
сравнение с предыдущим родителем. Операция просеивания вверх 
выполняется до тех пор, пока элемент не станет родителем,
удовлетворяющим условию кучи.

Извлечение минимума из кучи минимумов происходит следующим образом: 
удаляется корневой элемент (элемент с минимальным значением), а на его
место ставится последний элемент кучи. Затем выполняется операция
просеивания вниз для нового корневого элемента. Эта операция
заключается в том, что элемент сравнивается с его потомками. Если 
значение элемента больше значения одного из потомков, то элемент
меняется местами с потомком и продолжается сравнение с потомком. 
Операция просеивания вниз выполняется до тех пор, пока элемент 
не станет потомком, удовлетворяющим условию кучи.

Временная сложность любой операции O(logN).
'''

class BinaryHeap:

    def __init__(self):
        self.heap = []

    def add(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def extract_min(self):
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self.sift_down(0)
        return min_val
    
    def sift_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index - 1) // 2

    def sift_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.sift_down(smallest)
        
    def print(self):
        print(self.heap)


heap = BinaryHeap()
heap.add(3)
heap.add(1)
heap.add(4)
heap.add(1)
heap.print()
print(heap.extract_min()) 
heap.print()