class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize an adjacency list to store outgoing flights from each node
        adj = [[] for _ in range(n)]
        for s, d, pr in flights:
            # For each flight, add the destination and price to the source node’s list
            adj[s].append((d, pr))

        # Start with 0 stops taken
        stops = 0
        # Initialize the BFS queue with the source node and a cost of 0
        q = deque([(src, 0)])
        # Track the minimum cost to reach each node; initialize with infinity
        cost = [inf] * n

        # Continue BFS while within stop limit and queue is not empty
        while stops <= k and q:
            # Get the number of nodes to process at the current level (current stop count)
            sz = len(q)
            for _ in range(sz):
                # Pop a node and its total cost to reach from the queue
                node, price = q.popleft()
                # Explore all direct neighbors (flights from current node)
                for nbr, baseprice in adj[node]:
                    # If this new path to neighbor is more expensive than known, skip it
                    if price + baseprice > cost[nbr]: continue
                    # Found a cheaper way to reach neighbor, update the cost
                    cost[nbr] = price + baseprice
                    # Add neighbor to queue with updated cumulative cost
                    q.append((nbr, cost[nbr]))
            # Increase the stop count after finishing one BFS level
            stops += 1

        # If destination was never reached, return -1; else return the cheapest cost
        return -1 if cost[dst] == inf else cost[dst]
