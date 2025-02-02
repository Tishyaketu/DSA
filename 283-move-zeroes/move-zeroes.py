class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        last_non_zero_found_at = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[last_non_zero_found_at], nums[cur] = nums[cur], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1
