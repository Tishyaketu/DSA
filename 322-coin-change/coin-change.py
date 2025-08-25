class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 : return 0
        q = deque([(amount,0)])
        v = set([amount])
        while q:
          rem, c = q.popleft()
          for coin in coins:
            nxt = rem - coin
            if nxt == 0 : return c + 1
            if nxt > 0 and nxt not in v :
              v.add(nxt)
              q.append((nxt,c+1))
        return -1