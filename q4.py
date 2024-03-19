'''
Queue(Очередь) - абстрактный тип данных, представляющий собой
список элементов,организованных по принципу FIFO (First-In First-Out)

2 операции: Enqueue (Push) O(1), Dequeue (Pop) O(1) 

(везде O(1) потому что просто меняем ссылки и создаём новый элемент)

Deque(Дек: двусторонняя очередь) - абстрактный тип данных, 
в котором элементы можно добавлять/удалять как в начало, так и в конец.

4 операции: PushBack O(1), PopBack O(1), 
PushFront O(1), PopFront O(1) 

(везде О(1) потому что просто меняем ссылки и создаём новый элемент)

Общая оценка времени сложности для реализации очереди и дека на основе списка
будет O(n), где n - количество элементов в списке.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return temp.data

    def is_empty(self):
        return self.front is None

    def print(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
q.enqueue(344)
q.print()

print("------------------------------------------------------")

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def push_back(self, data):

        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def push_front(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def pop_back(self):
        if self.rear is None:
            print("Deque is empty")
            return None
        temp = self.rear
        self.rear = temp.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        return temp.data

    def pop_front(self):
        if self.front is None:
            print("Deque is empty")
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return temp.data

    def is_empty(self):
        return self.front is None

    def print(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

d = Deque()
d.push_back(1)
d.push_back(2)
d.push_front(23)
d.push_back(300)
d.push_front(0)
d.print()