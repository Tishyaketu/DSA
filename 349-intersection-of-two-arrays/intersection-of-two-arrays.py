class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n, m, i, j = len(nums1)-1, len(nums2)-1, 0, 0
        intersection = set()
        while i<=n and j<=m:
          if nums1[i]==nums2[j]:
            intersection.add(nums1[i])
            i+=1
            j+=1
          elif nums1[i]<nums2[j]: i+=1
          else: j+=1
        res = []
        for n in intersection:
          res.append(n)
        return res