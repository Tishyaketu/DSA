class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #1 create adjacency list to convert flights array into a graph
        adj = [[] for _ in range(n)]
        for flight in flights:
          adj[flight[0]].append((flight[1],flight[2]))
        #2 create the stops taken till now wala variable
        stops = 0
        #3 create the BFS queue, that is an array of tuples, where 1st element is the current stop and 2nd element is the cumulative cost of the node from the src parameter
        q = deque([(src,0)])
        #4 create an array of minCost of a node from src parameter
        minCost = [inf for _ in range(n)]
        #5 start the BFS
        while stops<=k and q:
          #6 take the length of queue to check the entire level of the graph and also to make sure stops get incremented only not after every node but after a level is finished
          sz = len(q)
          #7 iterate throught the current level
          for _ in range(sz):
            #8 popleft for BFS FIFO order, do not pop as it will be DFS LIFO
            node, cumulativeCost = q.popleft()
            #9 explore every nbr of the node
            for nbr,baseCost in adj[node]:
              #10 if the minCost is already less than the upcoming cost, avoid this nbr move on to next nbr
              if cumulativeCost+baseCost>minCost[nbr]: continue
              #11 if above isn't true proceed to update minCost & BFS queue
              minCost[nbr] = cumulativeCost+baseCost
              q.append((nbr,minCost[nbr]))
          #12 finally upate the stops count as all the nbrs at current level have been processed
          stops+=1
        # 13 once BFS is over return the result accordingly
        return -1 if minCost[dst]==inf else minCost[dst]