class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = nums1
        b = nums2
        i = m-1
        j = n-1
        for k in range(n+m-1,-1,-1):
          if j<0: break
          if i>=0 and a[i]>b[j]:
            a[k] = a[i]
            i-=1
          else:
            a[k] = b[j]
            j-=1
        