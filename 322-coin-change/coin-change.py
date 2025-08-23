class Solution:
  def coinChange(self,coins, amount):
    memo = {}

    def dfs(remaining):
        # Base case: exact match
        if remaining == 0:
            return 0
        # Base case: impossible
        if remaining < 0:
            return float('inf')
        # Already computed
        if remaining in memo:
            return memo[remaining]

        # Try all coins
        min_coins = float('inf')
        for coin in coins:
            res = dfs(remaining - coin)
            if res != float('inf'):
                min_coins = min(min_coins, res + 1)  # +1 for this coin

        memo[remaining] = min_coins
        return min_coins

    result = dfs(amount)
    return result if result != float('inf') else -1
