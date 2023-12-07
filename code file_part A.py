class Vertex:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.neighbors = {}

def add_neighbor(self, neighbor_key, weight=1):
        self.neighbors[neighbor_key] = weight

def remove_neighbor(self, neighbor_key):
    if neighbor_key in self.neighbors:
        del self.neighbors[neighbor_key]

def get_neighbors(self):
        return self.neighbors.keys()

def get_edge_weight(self, neighbor_key):
        return self.neighbors.get(neighbor_key)


class Graph:
    #represents an undirected weighted graph

    def __init__(self):
        #constructs an empty graph object
        self.vertices = {}
        pass

    def get_weight(self,k_u,k_v):
        #returns the weight of edge between k_u and k_v if it exists (None otherwise)
        if k_u in self.vertices and k_v in self.vertices[k_u].neighbors:
             return self.vertices[k_u].neighbors[k_v]
        else:
            return 0



    def add_vertex(self,k,v,neighbors=[]):
        #k, v: key and value for the new vertex
        #neighbors: the new vertex's neighbors, as a list of keys (defaults to empty)
        if k not in self.vertices:
             self.vertices[k] = Vertex(k,v)
        for neighbor in neighbors:
             self.add_edge(k,neighbor,1)
        pass


    def delete_vertex(self,k):
        #deletes the vertex corresponding to key k from the graph
        if k in self.vertices:
            for vertex in self.vertices.values():
                if k in vertex.neighbors:
                    del vertex.neighbors[k]
            del self.vertices[k]
        pass

    def add_edge(self,k_u,k_v,w):
        #adds an edge with weight w between the vertices corresponding to keys k_u, k_v (if it doesn't already exist)
        if k_u in self.vertices and k_v in self.vertices:
             self.vertices[k_u].neighbors[k_v] = w
             self.vertices[k_v].neighbors[k_u] = w
        pass

    def delete_edge(self,k_u,k_v):
        #deletes the edge between the vertices corresponding to keys k_u, k_v (if it exists)
        if k_u in self.vertices and k_v in self.vertices[k_u].neighbors:
             del self.vertices[k_u].neighbors[k_v]
             del self.vertices[k_v].neighbors[k_u]
        pass

class Map(Graph):

    def __init__(self,n,obstacles=[]):
        #creates a map representing the squares of n by n grid
        #optional argument: list of (x,y) locations indicating obstacles (cannot pass through)
        super().__init__()
        self.n = n
        self.obstacle = []
        #initialize grid vertices
        for x in range(n):
            for y in range(n):
                self.add_vertex((x, y), "open")
                #add edges to adjacent vertices
                if x > 0:
                    self.add_edge((x, y), (x - 1, y), 1)  # West
                if y > 0:
                    self.add_edge((x, y), (x, y - 1), 1)  # North
                if x < n - 1:
                    self.add_edge((x, y), (x + 1, y), 1)  # East
                if y < n - 1:
                    self.add_edge((x, y), (x, y + 1), 1)  # South
        pass
    
    def print_pretty(self):
        #prints a pretty ASCII picture of the map using different characters for "open" spaces and obstacles
        #can also show paths, start points, end points, etc
        for y in range(self.n):
            for x in range(self.n):
                if self.is_obstacle(x, y):
                    print("X", end=' ')
                else:
                    print("o", end=' ')
            print()
        pass

    def add_obstacle(self,x,y):
        #adds an obstacle at position (x,y) (if it doesn't already exist)
        if (x, y) in self.vertices:
            self.vertices[(x, y)].value = "obstacle"
        for neighbor_key in list(self.vertices[(x, y)].neighbors.keys()):
             self.delete_edge((x, y), neighbor_key)
        pass

    def remove_obstacle(self,x,y):
        #removes an obstacle at position (x,y) (if it exists)
        if (x, y) in self.vertices and self.vertices[(x, y)].value == "obstacle":
            self.vertices[(x, y)].value = "open"
        #restore edges
            if x > 0:
                self.add_edge((x, y), (x - 1, y), 1)
            if y > 0:
                self.add_edge((x, y), (x, y - 1), 1)
            if x < self.n - 1:
                self.add_edge((x, y), (x + 1, y), 1)
            if y < self.n - 1:
                self.add_edge((x, y), (x, y + 1), 1)
        pass

    def is_obstacle(self,x,y):
        #returns True if there is an obstacle at (x,y); otherwise returns False
        return (x, y) in self.vertices and self.vertices[(x, y)].value == "obstacle"
        pass
