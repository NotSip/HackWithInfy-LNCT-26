# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = {}
        slow= head
        count=0
        while slow:
            if slow in seen:
                return slow 
            seen[slow]=True
            slow = slow.next

        return None
        