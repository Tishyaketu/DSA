class Solution:
    def dfs(self,node,visited,adj):
      for nbr in adj[node]:
        if nbr not in visited:
          visited.add(nbr)
          self.dfs(nbr,visited,adj)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for edge in edges:
          adj[edge[0]].append(edge[1])
          adj[edge[1]].append(edge[0])
        visited = set()
        cc = 0
        # for every node in adj list
        for node in range(len(adj)):
        # if node not visited start dfs for the node
          if node not in visited:
            visited.add(node)
            self.dfs(node,visited,adj)
            # once node and its nbrs are visited increment connected components count
            cc+=1
        return cc
        