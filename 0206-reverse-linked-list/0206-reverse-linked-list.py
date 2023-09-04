# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev,curr,nextt=head,head.next,head.next.next

        while nextt:
            curr.next=prev
            prev,curr,nextt=curr,nextt,nextt.next
        
        curr.next=prev
        head.next=None
        return curr