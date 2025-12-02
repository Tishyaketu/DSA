class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        na, nb, n = len(A), len(B), len(A) + len(B)
        def solve(k,a_st,a_end,b_st,b_end):
          if a_st > a_end: return B[k - a_st]
          if b_st > b_end: return A[k - b_st]
          a_idx, b_idx = (a_st + a_end)//2, (b_st + b_end)//2
          a_val, b_val = A[a_idx], B[b_idx]
          if a_idx + b_idx < k:
            if a_val < b_val: return solve(k,a_idx+1,a_end,b_st,b_end)
            else: return solve(k,a_st,a_end,b_idx+1,b_end)
          else:
            if a_val < b_val: return solve(k,a_st,a_end,b_st,b_idx-1)
            else: return solve(k,a_st,a_idx-1,b_st,b_end)
        if n%2: return solve(n//2,0,na-1,0,nb-1)
        else: return (solve(n//2,0,na-1,0,nb-1) + solve((n//2)-1,0,na-1,0,nb-1))/2