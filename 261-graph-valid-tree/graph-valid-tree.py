class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1: return False
        adj = [[] for _ in range(n)]
        for A,B in edges:
          adj[A].append(B)
          adj[B].append(A)
        parDict = {0:-1}
        q = deque([0])
        while q:
          node = q.popleft()
          for nbr in adj[node]:
            if nbr==parDict[node]: continue
            if nbr in parDict: return False
            parDict[nbr] = node
            q.append(nbr)
        return len(parDict)==n