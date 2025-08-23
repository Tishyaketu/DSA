class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dictionary to memoize results for each 'remaining' amount
      memo = {}
      result = self.dfs(coins, amount, memo)
      return result if result != float('inf') else -1
    def dfs(self, coins, remaining, memo):
      # Base case: exact match
      if remaining == 0:
        return 0
      # Base case: overshoot
      if remaining < 0:
        return float('inf')
        # Already solved → return cached value
      if remaining in memo:
        return memo[remaining]
      # Try all coins
      min_coins = float('inf')
      for coin in coins:
        res = self.dfs(coins, remaining - coin, memo)
        if res != float('inf'):
          min_coins = min(min_coins, res + 1)  # +1 for using this coin
      memo[remaining] = min_coins
      return min_coins