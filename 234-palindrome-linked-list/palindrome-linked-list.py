# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = self.middle(head)
        rev_sh= self.rev_sh(middle.next)
        fp = head
        sp = rev_sh
        while sp:
          if fp.val!=sp.val: return False
          fp = fp.next
          sp = sp.next
        return True
    def middle(self,node):
      slow, fast = node, node
      while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
      return slow
    def rev_sh(self,node):
      prev = None
      curr = node
      while curr:
        nn = curr.next
        curr.next = prev
        prev = curr
        curr = nn
      return prev