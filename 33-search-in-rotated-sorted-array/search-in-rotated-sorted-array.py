from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        # find pivot: index of smallest element
        while left <= right:
            m = (left + right) // 2
            if nums[m] > nums[n - 1]:
                left = m + 1
            else:
                right = m - 1

        ans = self._binary_search(nums, 0, left - 1, target)
        if ans != -1:
            return ans
        return self._binary_search(nums, left, n - 1, target)

    def _binary_search(self, nums: List[int], l: int, r: int, target: int) -> int:
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1