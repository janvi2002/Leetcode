# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
#         for odd even indexes 
        odd=head
        even=head.next
#     for not lossing even index pointer
        even_head=even
        while even and even.next:
#      here we pointing odd index to odd then move the pointer 
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
#    at last odd.next is poinitng to even starting point
        odd.next=even_head
        return head