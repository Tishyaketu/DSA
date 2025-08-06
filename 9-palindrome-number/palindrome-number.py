class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        stack = []
        while x!=0:
          y = x%10
          stack.append(y)
          x = x//10
        return stack==stack[::-1]
        