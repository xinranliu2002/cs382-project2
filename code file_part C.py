from collections import deque
import heapq
class Map(Graph):
    
    def dijkstra_sssp(self, source):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[source] = 0
        priority_queue = [(0, source)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            for neighbor, weight in self.vertices[current_vertex].neighbors.items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
    
    def dijkstra_print_shortest_paths(self, distances):
        for y in range(self.n):
            for x in range(self.n):
                distance = distances[(x, y)]
                if distance == float('inf'):
                    print("X", end=' ')
                else:
                    print(distance, end=' ')
            print()

    def dijkstra_spsp(self, start, end):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        visited = set()
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            visited.add(current_vertex)

            if current_vertex == end:
                return distances, len(visited)

            for neighbor, weight in self.vertices[current_vertex].neighbors.items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, len(visited)
    
    def dijkstra_spsp_visit_order(self, start, end):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        visit_order = {vertex: None for vertex in self.vertices}
        visited = set()
        priority_queue = [(0, start)]
        order = 0

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_vertex in visited:
                continue
            visited.add(current_vertex)
            visit_order[current_vertex] = order
            order += 1

            if current_vertex == end:
                break

            for neighbor, weight in self.vertices[current_vertex].neighbors.items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return visit_order
    
    def dijkstra_print_shortest_path(self, visit_order):
        for y in range(self.n):
            for x in range(self.n):
                if (x, y) in visit_order and visit_order[(x, y)] is not None:
                    print(f"{visit_order[(x, y)]:2}", end=' ')
                else:
                    print(" X", end=' ')
            print()

    def bfs_spsp_visited(self, start, end):
        start_x, start_y = start
        end_x,end_y = end

        if self.is_obstacle(start_x,start_y) or self.is_obstacle(end_x,end_y):
            return None
        queue = deque([(start_x,start_y)])
        parents = {(start_x,start_y):None}
        visited = set()

        while queue:
            x,y = queue.popleft()
            visited.add((x,y))
            if (x, y) == (end_x, end_y):
                path = []
                while (x, y) != (start_x, start_y):
                    path.append((x, y))
                    x, y = parents[(x, y)]
                path.append((start_x, start_y))
                return len(visited)
            
            for neighbor in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if neighbor in self.vertices and neighbor not in parents and not self.is_obstacle(*neighbor):
                    parents[neighbor] = (x,y)
                    queue.append(neighbor)
        return len(visited)