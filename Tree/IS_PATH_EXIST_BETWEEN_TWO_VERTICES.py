# In a direct graph, write a program to check if there is exist a path between two vertices

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V=vertices
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def isReachable(self, s, d):
        visited = [False]* (self.V)
        queue= []
        queue.append(s)
        visited[s] = True
        
        while queue:
            current_v = queue.pop(0)
            if current_v == d:
                return True
            for i in self.graph[current_v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False
    

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

u, v = 1, 3
print(g.isReachable(u, v))
        

