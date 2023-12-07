from collections import deque
import heapq

class Map(Graph):
     
    def bfs_sssp(self, source_x, source_y):
            data = {(x, y): {'distance': None, 'parent': None} for x in range(self.n) for y in range(self.n)}
            queue = deque([(source_x, source_y)])
            data[(source_x, source_y)]['distance'] = 0

            while queue:
                x, y = queue.popleft()
                current_distance = data[(x, y)]['distance']
                for neighbor in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if neighbor in self.vertices and data[neighbor]['distance'] is None and not self.is_obstacle(*neighbor):
                        data[neighbor]['distance'] = current_distance + 1
                        data[neighbor]['parent'] = (x, y)
                        queue.append(neighbor)
            return data
    
    def print_shortest_paths(self, data):
        for y in range(self.n):
            for x in range(self.n):
                distance = data[(x, y)]['distance']
                if distance is None:
                    print("X", end=' ')
                else:
                    print(distance, end=' ')
            print()

    def bfs_spsp(self, start, end):
        start_x, start_y = start
        end_x,end_y = end

        if self.is_obstacle(start_x,start_y) or self.is_obstacle(end_x,end_y):
            return None
        queue = deque([(start_x,start_y)])
        parents = {(start_x,start_y):None}

        while queue:
            x,y = queue.popleft()
            if (x, y) == (end_x, end_y):
                path = []
                while (x, y) != (start_x, start_y):
                    path.append((x, y))
                    x, y = parents[(x, y)]
                path.append((start_x, start_y))
                return path[::-1] 
            
            for neighbor in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if neighbor in self.vertices and neighbor not in parents and not self.is_obstacle(*neighbor):
                    parents[neighbor] = (x,y)
                    queue.append(neighbor)
        return None
    
    def print_shortest_path(self, path):
        if path is None:
            print('No such path')
        else:    
            for y in range(self.n):
                for x in range(self.n):
                    if (x, y) in path:
                        print(path.index((x, y)), end=' ')
                    elif self.is_obstacle(x,y):
                        print('X',end=' ')
                    else:
                        print('o', end= ' ')
                print()
