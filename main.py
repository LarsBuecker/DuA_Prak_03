import sys

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
            graph = Graph(tokens[2])
            continue    
        
        # Add edges to the graph
        if len(tokens) > 2:
            for i in range(2, len(tokens) - 1):
                tmp = tokens[i].split("w")
                graph.addEdge(tokens[0], tmp[0], tmp[1])

    file.close()

    return graph

if __name__ == "__main__":
    graph = read_file()