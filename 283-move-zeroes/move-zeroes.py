class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        last_non_zero_found_at = 0
        for cur in range(len(nums)):
            # print('cur: ',cur)
            # print('last_non_zero_found_at: ',last_non_zero_found_at)
            if nums[cur] != 0:
                # print('nums[',cur,']',nums[cur])
                # print('nums[',last_non_zero_found_at,']',nums[last_non_zero_found_at])
                nums[last_non_zero_found_at], nums[cur] = nums[cur], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1
                # print('nums: ',nums)
                # print('last_non_zero_found_at: ',last_non_zero_found_at)