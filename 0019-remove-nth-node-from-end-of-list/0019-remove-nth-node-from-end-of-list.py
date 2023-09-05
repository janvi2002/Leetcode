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
        while n:
            fast=fast.next
            n-=1
        if fast.next==None:
            return head.next
        else:
            while fast and fast.next:
                fast=fast.next
                slow=slow.next
                
        slow.next=slow.next.next
        return dummy.next
            
            
            