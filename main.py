import sys
import collections

# Representation of a graph
class Graph:

    def __init__(self, vertices) -> None:
        self.vertices = vertices # Number of vertices
        self.graph = [] # dict to store the graph
    
    ''' Adds a new Edge to the Graph
    u: source
    v: destination
    w: weight
    '''
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        
        '''
        if v is not None:
            print("Added edge: %d, %d, %d" % (u, v, w))
        else:
            print("Added Vert without edge: ", u)
        '''

    # Finds a set of an element i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Unites two sets of x and y by rank
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # attach smaller rank tree under root of higher rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # if ranks are equal, then make on as root and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def mst(self):
        result = [] # resultant MST
        i = 0
        e = 0

        # sort all edges of the graph in non-decreasing order of their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Create vertice subsets with single elements
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        
        #Number of edges to be taken is equal to vertices-1
        while e < self.vertices - 1:
            # pick the smallest edge and increment the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # if including this edge does´t cause cycle, include it in the result 
            # and incement the index of result for the next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # else discard the edge
                
        minimumCost = 0
        #print("# Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            #print("%d -- %d == %d" % (u, v, weight))
        print("# Minimum Spanning Tree with weight", minimumCost)
        print("n =", self.vertices)
        tmp = {}
        result_s = sorted(result)
        #print(result_s)
        for data in result_s:
            d = tmp.get(data[0])
            if d is not None:
                d.append(str(data[1]) + "w" + str(data[2]))
                tmp[data[0]] = d
            else:
                tmp[data[0]] = [str(data[1]) + "w" + str(data[2])]

            # reverse edge
            d = tmp.get(data[1])
            if d is not None:
                d.append(str(data[0]) + "w" +str(data[2]))
                tmp[data[1]] = d
            else:
                tmp[data[1]] = [str(data[0]) + "w" + str(data[2])]
        tmp = collections.OrderedDict(sorted(tmp.items()))
        for key in tmp.keys():
            t_str = ""
            itemlist = tmp.get(key)
            for item in itemlist:
                t_str += item + " "
            print(str(key) + " : " + t_str)

def read_file() -> Graph:
    file = open(sys.argv[1])

    graph = None
    for line in file:
        # Pass the comment lines
        tokens = line.split(" ")
        if tokens[0] == "#":
            continue
        # Get the vertice count of the graph and create a new instance of Graph
        if tokens[0] == "n":
            graph = Graph(int(tokens[2]))
            continue    
        
        # Add edges to the graph
        if len(tokens) > 2:
            for i in range(2, len(tokens)):
                tmp = tokens[i].split("w")
                # Clamp weight to 10000
                if int(tmp[1]) > 10000:
                    tmp[1] = 10000
                graph.addEdge(int(tokens[0]), int(tmp[0]), int(tmp[1]))
        else:
            print("# Graph ist nicht zusammenhängend")
            print("n = " + str(graph.vertices))
            for i in range(0, graph.vertices):
                print(str(i) + " :")
            return None

    file.close()

    return graph

if __name__ == "__main__":
    graph = read_file()
    if graph is not None:
        graph.mst()