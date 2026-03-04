# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                break

        else:
            return None

        starting = head
        meeting = slow
        while starting != meeting:
            starting = starting.next
            meeting = meeting.next

        return starting
        