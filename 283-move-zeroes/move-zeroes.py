class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)

        # Count the zeroes
        num_zeroes = nums.count(0)

        # Make all the non-zero elements retain their original order.
        ans = [num for num in nums if num != 0]

        # Move all zeroes to the end
        ans.extend([0] * num_zeroes)

        # Copy back to the original list
        for i in range(n):
            nums[i] = ans[i]
