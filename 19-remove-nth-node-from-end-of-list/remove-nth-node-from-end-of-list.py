# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # corner cases adjust karay sathi dummy node at the beginning
        dummy = ListNode(0)
        dummy.next = head
        # have two pointers at dummy node
        first = dummy
        second = dummy
        # move first pointer 'n' distance apart from second
        for i in range(n+1):
          first = first.next
        # move 1st pointer till null, while maintaining 'n' distance in between
        while first:
          first = first.next
          second = second.next
        # skip the required node i.e. 2nd.next.next
        second.next = second.next.next
        # return dummy.next i.e. original required LL
        return dummy.next