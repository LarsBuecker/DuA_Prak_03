# Representation of a Node in a graph
# Holds an index and a list of nodes that are connected
class Node(object):

    '''
    :param index:   Index of the node
    '''
    def __init__(self, index) -> None:
        self.index = index
        self.next = []

# Representation of a Edge between two nodes
class Edge(object):
    
    ''' 
    :param start:   Index of the first node
    :param end:     Index of the second node
    :param weight:  Weight of the edge
    '''
    def __init__(self, start, end, weight) -> None:
        self.start = start
        self.end = end
        self.weight = weight

# Representation of a subtree of a graph
class Subset(object):

    def __init__(self):
        self.parent = 0 # Index of the root
        self.rank = 0   # Rank of the subtree

    ''' Finds a set of an element i
    :param subsets: List of subsets to search in
    :param i:       Index of the subsets root node
    '''
    def find(self, subsets, i):
        if subsets[i] != i:
            subsets[i].parent = self.find(subsets, subsets[i].parent)
        return subsets[i].parent

    ''' Unites two sets of x and y by rank
    :param subsets: List of subsets 
    :param x:       index of the first subset
    :param y:       index of the second subset
    '''
    def union(self, subsets, x, y):
        new_x = self.find(subsets, x)
        new_y = self.find(subsets, y)

        if subsets[new_x].rank < subsets[new_y].rank:
            subsets[new_x].parent = new_y
        elif subsets[new_x].rank < subsets[new_y].rank:
            subsets[new_y].parent = new_x
        else:
            subsets[new_y].parent = new_x
            subsets[new_x].rank += 1

    ''' Compares the weight of two edges
    :param edge1:   Reference of the first edge
    :param edge2:   Reference of the second edge
    :returns:       Returns True if the first edge has a higher weight as the second edge
    '''
    def compare(self, edge1: Edge, edge2: Edge) -> bool:
        return edge1.weight > edge2.weight

# Representation of a undirected graph
class Graph(object):

    '''
    :param vert_count:  Count of vertices in the graph
    '''
    def __init__(self, vert_count) -> None:
        self.vert_count = vert_count
        self.edges = []

    ''' Adds a new Edge to the Graph
    :param u:   Reference of the first node
    :param v:   Reference of the second node
    :param w:   Weight of the added edge
    '''
    def addEdge(self, u, v, w):
        self.edges.append([u, v, w])

    def kruskal_mst(self):
        pass

    def graph_to_string(self):
        pass