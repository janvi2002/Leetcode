# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(ptr):
            pre = None
            nex = None
            while ptr != None:
                nex = ptr.next
                ptr.next = pre
                pre = ptr
                ptr = nex
            return pre
        #using middle element and reverse approach
        if not head or not head.next:
            return True
        entry=head
        slow=head
        fast=head
        while fast.next != None and fast.next.next != None:
            slow=slow.next
            fast=fast.next.next
        
        slow.next=reverse(slow.next)
        slow=slow.next
        while slow:
            if entry.val!=slow.val:
                return False
            entry=entry.next
            slow=slow.next
        return True