class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1: return False
        adj = [[] for _ in range(n)]
        for edge in edges:
          adj[edge[0]].append(edge[1])
          adj[edge[1]].append(edge[0])
        seen = set()
        seen.add(0)
        q = deque([0])
        while q:
          node = q.popleft()
          print(adj[node])
          for nbr in adj[node]:
            if nbr in seen: continue
            seen.add(nbr)
            q.append(nbr)
        return len(seen)==n