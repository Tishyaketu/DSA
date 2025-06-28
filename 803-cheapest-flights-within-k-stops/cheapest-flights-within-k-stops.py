class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize an adjacency list to store outgoing flights from each node
        adj = [[] for _ in range(n)]
        for flight in flights:
          # For each flight, add the destination and price to the source node’s list
          adj[flight[0]].append((flight[1],flight[2]))
        # Start with 0 stops taken
        stops = 0
        # Initialize the BFS queue with the source node and a cost of 0
        q = deque([(src,0)])
        # Track the minimum cost to reach each node; initialize with infinity
        minCost = [inf for _ in range(n)]
        # Continue BFS while within stop limit and queue is not empty
        while stops<=k and q:
            # Get the number of nodes to process at the current level (current stop count), need this so that curr stop count is incremetned only after a level i.e. the enitre q is emptied and not after every node at lvl
            sz = len(q)
            for i in range(sz):
                # Pop a node and its total cost to reach from the queue/source
                node, cumulativeCost = q.popleft()
                # Explore all direct neighbors (flights from current node)
                for nbr, baseCost in adj[node]:
                    # If this new path to neighbor is more expensive than known, skip it
                    if cumulativeCost+baseCost>minCost[nbr]:continue
                    # Found a cheaper way to reach neighbor, update the cost
                    minCost[nbr] = cumulativeCost+baseCost
                    # Add neighbor to queue with updated cumulative cost
                    q.append((nbr,minCost[nbr]))
            # Increase the stop count after finishing one BFS level
            stops+=1
        # If destination was never reached, return -1; else return the cheapest cost
        return -1 if minCost[dst]==inf else minCost[dst]
        