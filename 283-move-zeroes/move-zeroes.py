class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for i in range(len(nums)):
          if nums[i]!=0:
            nums[l] = nums[i] #this is the most important step this signifies,  
            #simple realization is if the current element is non-0, its' correct position can at best be it's current position or a position earlier
            l+=1
        for i in range(l,len(nums)):
          nums[i] = 0
        return nums