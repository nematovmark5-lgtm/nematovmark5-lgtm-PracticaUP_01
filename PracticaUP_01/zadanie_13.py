from collections import deque

class GraphStructure:
    def __init__(self, vertices, directed=False):
        self.vertex_count = vertices
        self.is_directed = directed
        self.matrix = [[0] * vertices for _ in range(vertices)]
        self.adjacency = [[] for _ in range(vertices)]
    
    def add_edge_matrix(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.matrix[u][v] = weight
            if not self.is_directed:
                self.matrix[v][u] = weight
    
    def add_edge_list(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adjacency[u].append((v, weight))
            if not self.is_directed:
                self.adjacency[v].append((u, weight))
    
    def bfs_matrix(self, start):
        visited = [False] * self.vertex_count
        queue = deque([start])
        visited[start] = True
        traversal = []
        
        while queue:
            v = queue.popleft()
            traversal.append(v)
            
            for neighbor in range(self.vertex_count):
                if self.matrix[v][neighbor] != 0 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return traversal
    
    def bfs_list(self, start):
        visited = [False] * self.vertex_count
        queue = deque([start])
        visited[start] = True
        traversal = []
        
        while queue:
            v = queue.popleft()
            traversal.append(v)
            
            for neighbor, _ in self.adjacency[v]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return traversal
    
    def dfs_matrix(self, start):
        visited = [False] * self.vertex_count
        traversal = []
        
        def dfs_util(vertex):
            visited[vertex] = True
            traversal.append(vertex)
            
            for neighbor in range(self.vertex_count):
                if self.matrix[vertex][neighbor] != 0 and not visited[neighbor]:
                    dfs_util(neighbor)
        
        dfs_util(start)
        return traversal
    
    def dfs_list(self, start):
        visited = [False] * self.vertex_count
        traversal = []
        
        def dfs_util(vertex):
            visited[vertex] = True
            traversal.append(vertex)
            
            for neighbor, _ in self.adjacency[vertex]:
                if not visited[neighbor]:
                    dfs_util(neighbor)
        
        dfs_util(start)
        return traversal
    
    def shortest_path(self, start, end):
        if start == end:
            return [start], 0
        
        visited = [False] * self.vertex_count
        parent = [-1] * self.vertex_count
        queue = deque([start])
        visited[start] = True
        
        while queue:
            v = queue.popleft()
            
            if v == end:
                path = []
                while v != -1:
                    path.append(v)
                    v = parent[v]
                return path[::-1], len(path) - 1
            
            for neighbor, _ in self.adjacency[v]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = v
                    queue.append(neighbor)
        
        return [], -1
    
    def display_matrix(self):
        print("Матрица смежности:")
        print("   " + " ".join(f"{i:2}" for i in range(self.vertex_count)))
        for i in range(self.vertex_count):
            print(f"{i:2} " + " ".join(f"{self.matrix[i][j]:2}" for j in range(self.vertex_count)))
    
    def display_list(self):
        print("Список смежности:")
        for i in range(self.vertex_count):
            neighbors = ", ".join(f"{v}({w})" for v, w in self.adjacency[i])
            print(f"{i}: [{neighbors}]")
