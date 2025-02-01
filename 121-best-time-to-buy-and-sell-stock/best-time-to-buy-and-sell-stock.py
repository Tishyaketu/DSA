class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        for pr in prices:
          minPrice = min(pr,minPrice)
          diff = pr - minPrice
          maxProfit = max(maxProfit,diff)
        return maxProfit