'''
Точка сочленения в графе – это вершина, которая, если ее удалить из 
графа, приводит к разделению графа на две или более компоненты. Иными 
словами, это вершина, которая является ключевой для связности графа.

Алгоритм нахождения точек сочленения в графе:
1. Назначьте временные метки для всех вершин графа. Временная 
метка – это порядковый номер, который показывает, когда вершина была 
посещена в процессе обхода графа.
2. Начните обход графа из любой вершины. При посещении каждой вершины
запишите ее временную метку и сохраните ее в массиве.
3. Для каждой вершины графа определите ее наименьшую временную метку 
среди всех ее соседей. Если эта вершина – корень дерева обхода и имеет 
двух или более детей, то она является точкой сочленения. Если же эта 
вершина не является корнем дерева, то она является точкой сочленения, 
если ее наименьшая временная метка больше или равна временной 
метке текущей вершины.
4. Повторите шаги 2 и 3 для всех вершин графа.

Алгоритм нахождения точек сочленения основан на поиске мостов в графе. 
Мост – это ребро, которое, если его удалить из графа, приводит к 
разделению графа на две или более компоненты. В алгоритме нахождения 
точек сочленения мы используем тот факт, что точка сочленения – это 
вершина, которая является концом моста.
'''

class vertex:
    def __init__(self, key):
        self.neighbours = {} 
        self.key = key

    def add(self, key, edge): 
        self.neighbours [key] = edge
        
class graph:
    def __init__(self):
        self.root = {} 
        self.nbnodes = 0 
        self.curr = 0

    def add(self, key1, key2, edge=0): 
        if key1 not in self.root: 
            self.root[key1] = vertex(key1) 
            self.nbnodes += 1
        if key2 not in self.root: 
            self.root[key2] = vertex(key2) 
            self.nbnodes += 1

        self.root[key1].add(key2, edge)
        self.root[key2].add(key1, edge)

    def cutver(self):
        visited = set() 
        discovered = {} 
        low_vis = {} 
        parent = [] 
        result = []

        for vertex in self.root: 
            if vertex not in visited: 
                parent [vertex] = -1
                self._cutver(vertex, parent, visited, discovered, low_vis, result)
        print (result)

    def _cutver(self, vertex, parent, visited, discovered, low_vis, result):
        visited.add(vertex)
        discovered [vertex] = self.curr
        low_vis [vertex] = self.curr
        children = 0 
        self.curr+=1

        for neighbour in self.root [vertex]. neighbours:

            if neighbour not in visited: 
                parent[neighbour] = vertex
                children += 1
                self._cutver(neighbour, parent, visited, discovered, low_vis, result)
                low_vis[vertex] = min(low_vis [vertex], low_vis[neighbour])

                if children > 1 and parent[vertex] == -1: 
                    result.append(vertex)

                if parent[vertex] != -1 and low_vis [neighbour] >= discovered[vertex]:
                    result.append(vertex)

                elif neighbour != parent[vertex]:
                    low_vis[vertex] = min(low_vis [neighbour], discovered [vertex])
                    
if '__name__' == '__main__':
    a = graph()
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    a.add(A, B)
    a.add(A, C)
    a.add(B,D)
    a.add(D,C)
    a.add(C,E)
    a.cutver()