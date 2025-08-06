from typing import List
from collections import defaultdict

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        # Graph G: G[u][v] = 0 if original edge u -> v, 1 if reversed edge v -> u
        G = defaultdict(dict)
        for u, v in edges:
            G[u][v] = 0  # No reversal needed
            G[v][u] = 1  # Reversal needed if we want v -> u

        res = [-1] * n

        # First pass: DP to compute number of reversals from root (0) down the tree
        def dp(i: int, j: int) -> int:
            cur = 0
            for k, cost in G[j].items():
                if k == i:
                    continue
                cur += dp(j, k) + cost
            return cur

        # Second pass: DFS to adjust reversals count for each node
        def dfs(i: int, v: int):
            res[i] = v
            for j, cost in G[i].items():
                if res[j] < 0:
                    dfs(j, v - cost + G[j][i])

        dfs(0, dp(-1, 0))
        return res
