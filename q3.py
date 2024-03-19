'''
Стек - Абстрактный тип данных, представляющий собой список 
элементов,организованных по принципу 
LIFO (Last-In First-Out), похож на стопку тарелок.

Методы Стека:
1. push(item), добавляющий элемент на вершину стека
2. pop(), удаляющий самый верхний элемент стека и возвращающий его.
3. peek(), возвращающий самый верхний элемент стека.

'''


#Реализация Стека на основе динамического массива
class ArrayStack:
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        value = self.items[-1]
        self.items = self.items[-1]
        return value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def print(self):
        print(self.items)
   
st = ArrayStack()
st.push(34)
st.push(33)
st.push(4)
st.push(18)
print(st.peek())
st.print()
print("------------------------------------------------------")


#Реализация Стека на основе списка
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
    
    def push(self, item):
        self.top = Node(item, self.top)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        return data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data
    
    def size(self):
        current = self.top
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def print(self):
        curr = self.top
        while curr:
            print(curr.data)
            curr = curr.next

lst = LinkedStack()
lst.push(12)
lst.push(2)
lst.push(3248)
print(lst.pop())
print()
lst.print()