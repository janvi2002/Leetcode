# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n==1:
            return None
        dummy=ListNode(0)
        dummy.next=head
        fast=dummy
        slow=dummy
#         move the fast pointer till the given n
        while n:
            fast=fast.next
            n-=1
#      edge contiditon if it gives the n = length of linked list
        if fast.next==None:
            return head.next
        else:
#      move the both pointer one by one untill fast reaches to the Null
            while fast and fast.next:
                fast=fast.next
                slow=slow.next
        slow.next=slow.next.next
        return dummy.next
            
            
            