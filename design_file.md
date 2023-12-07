# Design Document
Group Member: Xinran Liu

## Part A: Implementations of Graph and Map

### Use of Adjacency List
In this implementation, the graph is represented using the adjacency list structure. Each vertex in the graph is stored as an object in a dictionary (self.vertices), with the vertex key as the dictionary key and the vertex object as the value. The vertex object includes the vertex key, its value, and another dictionary (neighbors) to store adjacent vertices and their corresponding edge weights.

The adjacency list was chosen as it allows for quick lookup of vertices and their neighbors and efficient addition and removal of vertices and edges. The use of dictionaries for both vertices and their neighbors enables constant time complexity for basic operations like adding a vertex, checking for the existence of a vertex, or retrieving a vertex's neighbors and edge weights.

### Graph Implementation Tutorial
The steps below demonstrate how we use our graph implementation:

1. Create an empty graph
```
graph = Graph()
```

2. Add vertices A and B
```
graph.add_vertex('A', 'ValueA')
graph.add_vertex('B', 'ValueB')
```
3. Add an edge between vertex A and B of weight 3
```
graph.add_edge('A', 'B', 3)
```
4. Add another vertex C and connect with vertex A, the edge has default value 1
```
graph.add_vertex('C', 'ValueC', ['A'])
```
5. Check the weight of the edge between vertex A and C
```
graph.get_weight('A', 'C')
output: 1
```
6. Update the weight of the edge between vertex A and C
```
graph.add_edge('A','C',2)
```
7. Remove the edge between vertex A and B
```
graph.delete_vertex('B')
```
8. Remove the vertex B
```
graph.delete_vertex('B')
```

### Map implementation tutorial
In the Map class, obstacles are represented by modifying the value of the vertex to indicate an obstacle and removing all edges incident to that vertex. This approach effectively makes the vertex inaccessible, simulating an obstacle. When an obstacle is removed, edges are re-added to restore connectivity.

Below steps demonstrate how we use our map implementation:
1. Create a 4-by-4 new map
```
map = Map(4)
```
2. Add an obstacle at space (1,1),(2,2),(0,2)
```
map.add_obstacle(1, 1)
map.add_obstacle(2, 2)
map.add_obstacle(0, 2)
```
3. Check whether the obstacle is added at (1,1)
```
map.is_obstacle(1,1)
output: True
```
4. Display a picture of map
```
map.print_pretty()
```
![Fig 1. Creating new map](https://github.com/xinranliu2002/cs382-project2/figures
/fig1.png)

## Part B: Breadth First Search

### BFS-SSSP

Below steps demonstrate the bfs_sssp function:
1. Create an unweighted map with several obstacles
```
map = Map(5)
map.add_obstacle(1,1)
map.add_obstacle(3,2)
map.print_pretty()
```

2. Calculate the shortest paths from source (1,2) to each space
```
paths = map.bfs_sssp(1,2)
map.print_shortest_paths(paths)
```

### BFS-SPSP
Below steps demonstrate the bfs_sssp function:
1. Use the same map as above
2. Calculate the shortest path from (1,2) to (4,2)
```
path = map.bfs_spsp((1,2),(4,2))
map.print_shortest_path(path)
```

## Part C: Weighted Graphs

### Dijkstra-SSSP
Below steps demonstrate the dijkstra_sssp function:
1. Create a weighted map with several obstacles and weighted edges
```
map = Map(5)
map.add_obstacle(1,1)
map.add_obstacle(3,2)
map.add_edge((0,2),(1,2),4)
map.add_edge((3,3),(4,3),4)
```
2. Calculate the shortest paths from source (1,2) to each space
```
paths = map.dijkstra_sssp((1,2))
map.dijkstra_print_shortest_paths(paths)
```

###

