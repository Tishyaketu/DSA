class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        q = deque([(amount,0)])
        v = set([amount])
        while q:
          rem, c = q.popleft()
          for coin in coins:
            nxt_amt = rem - coin
            if nxt_amt == 0 : return c + 1
            if nxt_amt > 0 and nxt_amt not in v:
              v.add(nxt_amt)
              q.append((nxt_amt,c+1))
        return -1