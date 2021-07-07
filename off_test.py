from collections import defaultdict

class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []    
     
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    def KruskalMST(self):
 
        result = []
 
        i = 0
        e = 0
 
        self.graph =  sorted(self.graph, key=lambda item: item[2])
 
        parent, rank = [], []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
     
        while e < self.V-1:	
            u, v, w =  self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            if x != y:
                e += 1  
                result.append([u, v, w])
                self.union(parent, rank, x, y)          
 
        print("Following are the edges in the constructed MST")
        for u, v, weight in result:
            print("%d - %d = %d" % (u, v, weight))
 
 
g = Graph(8)
g.addEdge(0, 2, 5270)
g.addEdge(0, 3, 7806)
g.addEdge(0, 4, 840)
g.addEdge(0, 5, 2778)
g.addEdge(0, 7, 5740)
g.addEdge(1, 2, 4606)
g.addEdge(1, 4, 4881)
g.addEdge(1, 5, 6612)
g.addEdge(2, 0, 5720)
g.addEdge(2, 1, 4606)
g.addEdge(2, 4, 8645)
g.addEdge(2, 6, 1633)
g.addEdge(2, 7, 2210)
g.addEdge(3, 0, 7806)
g.addEdge(4, 0, 840)
g.addEdge(4, 1, 4881)
g.addEdge(4, 2, 8645)
g.addEdge(4, 6, 1633)
g.addEdge(4, 7, 2210)
g.addEdge(5, 0, 2778)
g.addEdge(5, 1, 6612)
g.addEdge(5, 3, 9007)
g.addEdge(6, 2, 1633)
g.addEdge(6, 3, 7161)
g.addEdge(6, 4, 9230)
g.addEdge(7, 0, 5740)
g.addEdge(7, 2, 2210)

g.KruskalMST()