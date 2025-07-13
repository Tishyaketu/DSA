class Solution:
    def dfs(self, adj_list, visited, src):
        visited[src] = True
        for neighbor in adj_list[src]:
            if not visited[neighbor]:
                self.dfs(adj_list, visited, neighbor)
    
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        if n == 0:
            return 0
        
        components = 0
        visited = [False] * n
        adj_list = [[] for _ in range(n)]
        
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        for i in range(n):
            if not visited[i]:
                components += 1
                self.dfs(adj_list, visited, i)
        
        return components