## Part A Design Document
Group Member: Xinran Liu

# Adjacency List
In this implementation, the graph is represented using an adjacency list structure. Each vertex in the graph is stored as an object in a dictionary (self.vertices), with the vertex key as the dictionary key and the vertex object as the value. The vertex object includes the vertex key, its value, and another dictionary (neighbors) to store adjacent vertices and their corresponding edge weights.

This adjacency list was chosen due to its efficiency in storing sparse graphs, where the number of edges is significantly less than the number of possible edges. It allows for quick lookup of vertices and their neighbors and efficient addition and removal of vertices and edges. The use of dictionaries for both vertices and their neighbors enables constant time complexity for basic operations like adding a vertex, checking for the existence of a vertex, or retrieving a vertex's neighbors and edge weights.

# Obstacles in Maps
In the Map class, obstacles are represented by modifying the value of the vertex to indicate an obstacle and removing all edges incident to that vertex. This approach effectively makes the vertex inaccessible, simulating an obstacle. When an obstacle is removed, edges are re-added to restore connectivity.

# Forward Plans
By Nov 25: 
1. Check initializations with some graph demos
2. Finish Part A Design Document

By Nove 28:
1. Study the Queue data structure in Python
2. Write code for BFS functions

By Dec 2:
1. Finish up with the four functions
2. Write up Design document for part B
