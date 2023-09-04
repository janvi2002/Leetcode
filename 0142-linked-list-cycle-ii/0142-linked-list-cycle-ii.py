# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
                return None
        fast = head
        slow = head
        entry = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
#  here again we move one one step untill it get collide to find the starting index
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                return slow
        return None