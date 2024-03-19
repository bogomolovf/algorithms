'''
Односвязный список - структура данных, состоящая из узлов, каждый из которых
имеет ссылку на следующий узел.

Двусвязный список - структура данных, состоящая из узлов, каждый из которых
имеет ссылки на следующий и предыдущий узлы.

'''
#Реализация односвязного списка
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getNextNode(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head = None

#Добавление элемента в односвязный список
    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

#Удаление элемента из односвязного списка
    def remove(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()
            
lin = LinkedList()
lin.add(3434)
lin.add(12)
lin.add(3)
lin.remove(12)
lin.print()


#Реализация двусвязного списка
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
    def getNextNode(self):
        return self.next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

#Добавление элемента в двусвязный список
    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

#Удаление элемента из двусвяхного списка
    def remove(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                current.next.prev = current
                return
            current = current.next

    def print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()

dab = DoublyLinkedList()
dab.add(44)
dab.add(55)
dab.add(112)
dab.remove(44)
dab.print()
