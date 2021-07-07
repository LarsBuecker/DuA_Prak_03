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

# Representation of a undirected graph
class Graph(object):

    '''
    :param vert_count:  Count of vertices in the graph
    '''
    def __init__(self, vert_count) -> None:
        self.vert_count = vert_count
        self.edges = []

    '''
    :param u:   Reference of the first node
    :param v:   Reference of the second node
    :param w:   Weight of the added edge
    '''
    def addEdge(self, u, v, w):
        pass

    def kruskal_mst(self):
        pass

    def graph_to_string(self):
        pass