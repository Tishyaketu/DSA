from collections import deque
class Solution:

  def coinChange(self,coins, amount):
    if amount == 0:
        return 0

    # queue holds tuples: (remaining_amount, number_of_coins_used)
    queue = deque([(amount, 0)])
    visited = set([amount])  # to avoid revisiting the same amount

    while queue:
        remaining, steps = queue.popleft()

        # Try every coin
        for coin in coins:
            next_amount = remaining - coin
            if next_amount == 0:
                return steps + 1  # Found solution
            if next_amount > 0 and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, steps + 1))

    return -1  # Not possible
