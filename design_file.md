# Design Document
Group Member: Xinran Liu

## Part A: Implementations of Graph and Map

### Use of Adjacency List
In this implementation, the graph is represented using the adjacency list structure. Each vertex in the graph is stored as an object in a dictionary (self.vertices), with the vertex key as the dictionary key and the vertex object as the value. The vertex object includes the vertex key, its value, and another dictionary (neighbors) to store adjacent vertices and their corresponding edge weights.

The adjacency list was chosen as it allows for quick lookup of vertices and their neighbors and efficient addition and removal of vertices and edges. The use of dictionaries for both vertices and their neighbors enables constant time complexity for basic operations like adding a vertex, checking for the existence of a vertex, or retrieving a vertex's neighbors and edge weights.

### Graph Implementation Tutorial
The steps below demonstrate how we use our graph implementation:

1. Create an empty graph.
```
graph = Graph()
```

2. Add vertices A and B.
```
graph.add_vertex('A', 'ValueA')
graph.add_vertex('B', 'ValueB')
```
3. Add an edge between vertex A and B of weight 3.
```
graph.add_edge('A', 'B', 3)
```
4. Add another vertex C and connect with vertex A, the edge has default value 1.
```
graph.add_vertex('C', 'ValueC', ['A'])
```
5. Check the weight of the edge between vertex A and C.
```
graph.get_weight('A', 'C')
output: 1
```
6. Update the weight of the edge between vertex A and C.
```
graph.add_edge('A','C',2)
```
7. Remove the edge between vertex A and B.
```
graph.delete_vertex('B')
```
8. Remove the vertex B.
```
graph.delete_vertex('B')
```

### Map implementation tutorial
In the Map class, obstacles are represented by modifying the value of the vertex to indicate an obstacle and removing all edges incident to that vertex. This approach effectively makes the vertex inaccessible, simulating an obstacle. When an obstacle is removed, edges are re-added to restore connectivity.

Below steps demonstrate how we use our map implementation:
1. Create a 4-by-4 new map.
```
map = Map(4)
```
2. Add an obstacle at space (1,1),(2,2),(0,2).
```
map.add_obstacle(1, 1)
map.add_obstacle(2, 2)
map.add_obstacle(0, 2)
```
3. Check whether the obstacle is added at (1,1).
```
map.is_obstacle(1,1)
output: True
```
4. Display a picture of map.
```
map.print_pretty()
```
![Fig 1. Creating new map](https://github.com/xinranliu2002/cs382-project2/blob/main/figures/fig1.png)

## Part B: Breadth First Search

### BFS-SSSP

Below steps demonstrate the bfs_sssp function:
1. Create an unweighted 5 $\times$ 5 map with obstacles at (1,1),(3,2).
```
map = Map(5)
map.add_obstacle(1,1)
map.add_obstacle(3,2)
map.print_pretty()
```
![Fig 2. a 5 $\times$ 5 Map with obstacles at (1,1),(3,2)](https://github.com/xinranliu2002/cs382-project2/blob/main/figures/fig2.png)

2. Calculate the shortest paths from source (1,2) to each space.
   
The function `bfs_sssp` takes as an argument a map and a source point

The function `print_shortest_paths` takes a map and the calculated paths as arguments
```
paths = map.bfs_sssp(1,2)
map.print_shortest_paths(paths)
```
![Fig 3. a 5 $\times$ 5 Map with obstacles at (1,1),(3,2)](https://github.com/xinranliu2002/cs382-project2/blob/main/figures/fig3.png)
### BFS-SPSP
Below steps demonstrate the bfs_sssp function:
1. Use the same map as above.
2. Calculate the shortest path from (1,2) to (4,2).

The function `bfs_spsp` takes as a map, a start point, and an end point as arguments;

The function `print_shortest_path` takes a map and the calculated path as arguments.
```
path = map.bfs_spsp((1,2),(4,2))
map.print_shortest_path(path)
```
![Fig 4. a 5 $\times$ 5 Map with obstacles at (1,1),(3,2)](https://github.com/xinranliu2002/cs382-project2/blob/main/figures/fig4.png)

## Part C: Dijkstra Algorithms

### Dijkstra-SSSP
Below steps demonstrate the dijkstra_sssp function:
1. Create a weighted 5 $\times$ 5 map with obstacles at (1,1),(3,2) and weighted edges.
```
map = Map(5)
map.add_obstacle(1,1)
map.add_obstacle(3,2)
map.add_edge((0,2),(1,2),4)
map.add_edge((3,3),(4,3),4)
```
2. Calculate the shortest paths from source (1,2) to each space.
```
paths = map.dijkstra_sssp((1,2))
map.dijkstra_print_shortest_paths(paths)
```
![Fig 5. a 5 $\times$ 5 Map with obstacles at (1,1),(3,2)](https://github.com/xinranliu2002/cs382-project2/blob/main/figures/fig5.png)

### Dijkstra-SPSP
Below steps demonstrate the dijkstra_spsp function:
1. Use the same weighted map as above.
2. Calculate the shortest path from (1,2) to (4,2).
The function `dijkstra_spsp` takes a map, a start point, and an end point as arguments. It outputs a shortest path, and a set of vertices that are visited before we find such path.
```
path, visited = map.dijkstra_spsp((1,2),(4,2))
```
3. Display the order in which the vertices are visited.

The function `dijkstra_spsp_visit_order` takes a map, a start point, and an end point as arguments. It outputs a list what record the visit order of each vertex in the map.

The function `print_dijkstra_visit_order` takes the calculated visit order as argument.

```
visit_order = map.dijkstra_spsp_visit_order((1,2),(4,2))
map.dijkstra_print_shortest_path(visit_order)
```
![Fig 6. a 5 $\times$ 5 Map with obstacles at (1,1),(3,2)](https://github.com/xinranliu2002/cs382-project2/blob/main/figures/fig6.png)


